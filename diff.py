diff --git a/lms/djangoapps/slidder/models.py b/lms/djangoapps/slidder/models.py
index f815eb3..c30000a 100644
--- a/lms/djangoapps/slidder/models.py
+++ b/lms/djangoapps/slidder/models.py
@@ -1,18 +1,24 @@
 from django.db import models
 from openedx.core.djangoapps.content.course_overviews.models import CourseOverview
 from openedx.core.djangoapps.xmodule_django.models import CourseKeyField
-
+from django.conf import settings
 
 
 class indexslidder(models.Model):
+	config = settings.VERIFY_STUDENT['SOFTWARE_SECURE']
+	url=config['STORAGE_KWARGS']['custom_domain']+"/"+settings.AWS_STORAGE_BUCKET_NAME
 	# course = CourseKeyField(db_index=True, primary_key=True, max_length=255)
 	title_in_english =  models.CharField(max_length=300)
 	title_in_arabic =  models.CharField(max_length=300)
 	description_in_english = models.CharField(max_length=800)
 	description_in_arabic = models.CharField(max_length=800)
-	arabic_image = models.ImageField(upload_to="media")
-	english_image = models.ImageField(upload_to="media")
+	arabic_image = models.ImageField()
+	english_image = models.ImageField()
 	button_text_in_english = models.CharField(max_length=30)
 	button_text_in_arabic = models.CharField(max_length=30)
-	link = models.CharField(max_length=800,null=True,blank=True)
+	link_arabic = models.CharField(max_length=800,null=True,blank=True)
+	link_english = models.CharField(max_length=800,null=True,blank=True)
+
+	def __unicode__(self):
+		return self.title_in_english
 
diff --git a/lms/djangoapps/verify_student/views.py b/lms/djangoapps/verify_student/views.py
index 3997a8d..1f7b8a0 100644
--- a/lms/djangoapps/verify_student/views.py
+++ b/lms/djangoapps/verify_student/views.py
@@ -184,8 +184,8 @@ class PayAndVerifyView(View):
     WEBCAM_REQ = "webcam-required"
 
     STEP_REQUIREMENTS = {
-        # ID_PHOTO_STEP: [PHOTO_ID_REQ, WEBCAM_REQ],
-        # FACE_PHOTO_STEP: [WEBCAM_REQ]
+        ID_PHOTO_STEP: [PHOTO_ID_REQ, WEBCAM_REQ],
+       # FACE_PHOTO_STEP: [WEBCAM_REQ]
     }
 
     # Deadline types
diff --git a/lms/templates/verify_student/make_payment_step.underscore b/lms/templates/verify_student/make_payment_step.underscore
index 727b7bf..0e7895f 100644
--- a/lms/templates/verify_student/make_payment_step.underscore
+++ b/lms/templates/verify_student/make_payment_step.underscore
@@ -28,7 +28,7 @@
         <%- gettext( "You can now enter your payment information and complete your enrollment." ) %>
       </div>
     <% } %>
-
+    <%-verificationDeadline%>
     <div class="instruction <% if ( !upgrade && isActive ) { %>center-col<% } %>">
       <% if ( _.some( requirements, function( isVisible ) { return isVisible; } ) ) { %>
       <p class="instruction-info">
@@ -147,6 +147,7 @@
   <div class="payment-buttons nav-wizard is-ready center">
     <input type="hidden" name="contribution" value="<%- minPrice %>" />
     <input type="hidden" name="sku" value="<%- sku %>" />
+   <input type="hidden" name="processors" value="<%- processors %>" />
     <div class="purchase">
       <p class="product-info"><span class="product-name"></span> <%- gettext( "price" ) %>: <span class="price"><%- minPrice %> SAR</span></p>
     </div>
@@ -162,7 +163,7 @@
 </div>
 
 <script>
-
+debugger;
 x=JSON.parse($("#pay-and-verify-container").attr("data-user-country"))
     for (var i =0; i < x.length; i++) {
        $("#country").append("<option value=" +x[i][0] + ">"+x[i][1]+"</option>")
@@ -173,4 +174,4 @@ y = "<%- selected_country %>"
 x=$('#country option[value=' + y +']')
 x.attr("selected","selected")
 
-</script>
\ No newline at end of file
+</script>
diff --git a/themes/kkux/lms/templates/dashboard/_dashboard_course_listing.html b/themes/kkux/lms/templates/dashboard/_dashboard_course_listing.html
index 85b6ce4..bc287ef 100644
--- a/themes/kkux/lms/templates/dashboard/_dashboard_course_listing.html
+++ b/themes/kkux/lms/templates/dashboard/_dashboard_course_listing.html
@@ -91,11 +91,17 @@ from util.course import get_link_for_about_page, get_encoded_course_sharing_utm_
     </div>
       <div class="wrapper-course-details">
         <h3 class="course-title">
+          <%
+              if LANGUAGE_CODE == 'ar':
+                  course_display_name = course_overview.display_name_in_arabic
+              else:
+                  course_display_name = course_overview.display_name_with_default   
+          %>
           % if show_courseware_link:
             % if not is_course_blocked:
-              <a data-course-key="${enrollment.course_id}" href="${course_target}">${course_overview.display_name_with_default}</a>
+              <a data-course-key="${enrollment.course_id}" href="${course_target}">${course_display_name}</a>
             % else:
-              <a class="disable-look" data-course-key="${enrollment.course_id}">${course_overview.display_name_with_default}</a>
+              <a class="disable-look" data-course-key="${enrollment.course_id}">${course_display_name}</a>
             % endif
           % else:
             <span>${course_overview.display_name_with_default}</span>
diff --git a/themes/kkux/lms/templates/index.html b/themes/kkux/lms/templates/index.html
index d67acfd..e87b75c 100644
--- a/themes/kkux/lms/templates/index.html
+++ b/themes/kkux/lms/templates/index.html
@@ -10,6 +10,7 @@ from django.utils.translation import ugettext as _
 from django.conf import settings
 from lms.djangoapps.ccx.overrides import get_current_ccx
 from openedx.core.djangolib.markup import HTML, Text
+import boto3
 
 # App that handles subdomain specific branding
 from branding import api as branding_api
@@ -35,13 +36,34 @@ from openedx.core.djangoapps.content.course_overviews.models import CourseOvervi
     <section class="section-banner">
       <div class="main-story">
         % for data in slidderdata:
-      
+	 <% 
+                conn = boto3.client('s3',aws_access_key_id=settings.AWS_ACCESS_KEY_ID,aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,)
+                arabic_image=data.arabic_image.url.split("/")[-1]
+                english_image=data.english_image.url.split("/")[-1]
+                arabic_image_url = conn.generate_presigned_url(
+                     'get_object',
+                     Params = {
+                            'Bucket': settings.AWS_STORAGE_BUCKET_NAME ,
+                            'Key':arabic_image
+                        },
+                    
+                 )
+
+                english_image_url = conn.generate_presigned_url(
+                     'get_object',
+                     Params = {
+                            'Bucket': settings.AWS_STORAGE_BUCKET_NAME ,
+                            'Key': english_image
+                        },
+                    
+                 )
+            %>      
         <div>
             <div class="story-slide">
                 % if LANGUAGE_CODE == 'ar':
-                <img src="${data.arabic_image}" class="img-responsive" alt="image">
+                <img src="${arabic_image_url}" class="img-responsive" alt="image">
                 % else:
-                <img src="${data.english_image}" class="img-responsive" alt="image">
+                <img src="${english_image_url}" class="img-responsive" alt="image">
                 % endif
                 <div class="story-slide-txt">
                     <div class="container">
@@ -60,15 +82,17 @@ from openedx.core.djangoapps.content.course_overviews.models import CourseOvervi
                         % endif
                         </p>
                         <div class="learn-more">
-                            % if data.link:
-                                <a href="${reverse('about_course', args=[data.link]) if banner_design else '#'}">
-                                    % if LANGUAGE_CODE == 'ar':
-                                        ${data.button_text_in_arabic}
-                                    % else:
+				% if  LANGUAGE_CODE == 'ar' and data.link_arabic != '':
+                                	<a href="${data.link_arabic}">
+
+		
+                                       ${data.button_text_in_arabic}
+                               % elif data.link_english != '':
+					 <a href="${data.link_english}">
+
                                         ${data.button_text_in_english}
-                                    % endif
+                               % endif
                                 </a>
-                            %endif 
                         </div>
                     </div>
                 </div>
