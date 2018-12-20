"""Program reindex"""

import pytz
import json
import requests
import logging
from datetime import datetime

from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from opaque_keys.edx.keys import CourseKey
from search.search_engine_base import SearchEngine
from .models import Program
log = logging.getLogger('edx.modulestore')


@user_passes_test(lambda u: u.is_superuser)
def index_programs_information(request):
    """
    Add all the program to the course discovery index

    """
    INDEX_NAME = "courseware_index"
    searcher = SearchEngine.get_search_engine(INDEX_NAME)
    if not searcher:
        return

    programs = Program.objects.all()
    for program in programs:
        if program.start <= datetime.now(pytz.UTC).date():
            program_info = {
                'id': program.id,
                'course': program.id,
                'content': {
                    'display_name': program.name,
                    'overview': program.short_description
                },
                'image_url': program.banner_image.url,
                'start': program.start,
                'language': program.language.code,
                'subject': program.subject.name,
                'is_program': True,
            }
        # Broad exception handler to protect around and report problems with indexing
            try:
                searcher.index('course_info', [program_info])
            except:  # pylint: disable=bare-except
                log.exception(
                    "Program discovery indexing error encountered %s",
                    program_info.get('id', ''),
                )
                return JsonResponse({
                    'success': False,
                    'error': 'Program discovery indexing error encountered ',
                    'Program': program.name
                })
        else:
            return JsonResponse({
                    'success': False,
                    'error': 'This ' + program.name + ' program start date is in future: ' + str(program.start),
                    'suggestion': 'Please set past progrm start date',
                    'Program': program.name
                })

    return redirect(reverse('show-programs'))


def index_course_programs(course_id):
    """
    reindex only the program that containts course

    """
    INDEX_NAME = "courseware_index"
    searcher = SearchEngine.get_search_engine(INDEX_NAME)
    if not searcher:
        return
    course_key = CourseKey.from_string(course_id)
    programs = Program.objects.filter(courses__course_key=course_key)
    for program in programs:
        program_banner_image_url = program.banner_image.url if program.banner_image else '/static/images/banner-black-background.jpg'
        if program.start <= datetime.now(pytz.UTC).date():
            program_info = {
                'id': program.id,
                'course': program.id,
                'content': {
                    'display_name': program.name,
                    'overview': program.short_description
                },
                'image_url': program_banner_image_url,
                'start': program.start,
                'language': program.language.code,
                'subject': program.subject.name,
                'is_program': True,
            }
        # Broad exception handler to protect around and report problems with indexing
            try:
                searcher.index('course_info', [program_info])
            except:  # pylint: disable=bare-except
                log.exception(
                    "Program discovery indexing error encountered %s",
                    program_info.get('id', ''),
                )
                return JsonResponse({
                    'success': False,
                    'error': 'Program discovery indexing error encountered ',
                    'Program': program.name
                })
        else:
            return JsonResponse({
                    'success': False,
                    'error': 'This ' + program.name + ' program start date is in future: ' + str(program.start),
                    'suggestion': 'Please set past progrm start date',
                    'Program': program.name
                })
    return True


@user_passes_test(lambda u: u.is_superuser)
def reindex_specific_program(request, pk):
    """
    reindex specific program

    """
    INDEX_NAME = "courseware_index"
    searcher = SearchEngine.get_search_engine(INDEX_NAME)
    if not searcher:
        return

    try:
        program = Program.objects.get(pk=pk)
    except Exception, e:
        return JsonResponse({
                'success': False,
                'error': 'Program not found in this id ' + pk,
            })

    if program.start <= datetime.now(pytz.UTC).date():
        program_banner_image_url = program.banner_image.url if program.banner_image else '/static/images/banner-black-background.jpg'
        program_info = {
            'id': program.id,
            'course': program.id,
            'content': {
                'display_name': program.name,
                'overview': program.short_description
            },
            'image_url': program_banner_image_url,
            'start': program.start,
            'language': program.language.code,
            'subject': program.subject.name,
            'is_program': True,
        }
    # Broad exception handler to protect around and report problems with indexing
        try:
            searcher.index('course_info', [program_info])
        except:  # pylint: disable=bare-except
            log.exception(
                "Program discovery indexing error encountered %s",
                program_info.get('id', ''),
            )
            return JsonResponse({
                'success': False,
                'error': 'Program discovery indexing error encountered ',
                'Program': program.name
            })
    else:
        return JsonResponse({
                'success': False,
                'error': 'This ' + program.name + ' program start date is in future: ' + str(program.start),
                'suggestion': 'Please set past progrm start date',
                'Program': program.name
            })

    return redirect(reverse('show-programs'))


def remove_program_elasticsearch(program_id=None, all_program=False):
    """
    Remove program from courses page(elasticsearch).
    Args:
        program_id: remove specific program
        all_program: remove all programs
    """
    headers = {'content-type': 'application/json'}
    elasticsearch_url = "http://localhost:9200/courseware_index/course_info/_query"
    # for single program
    if program_id:
        payload = {"term": {"course": program_id}}

    # remove all programs
    if all_program:
        payload = {"term": {"is_program": True}}
    requests.delete(elasticsearch_url, data=json.dumps(payload), headers=headers)
