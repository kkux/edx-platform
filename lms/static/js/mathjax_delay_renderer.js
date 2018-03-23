// Once generated by CoffeeScript 1.9.3, but now lives as pure JS
/* eslint-disable */
// TODO: Examine all of the xss-lint exceptions
(function() {
  var getTime;

  getTime = function() {
    return new Date().getTime();
  };

  this.MathJaxDelayRenderer = (function() {
    var bufferId, numBuffers;

    MathJaxDelayRenderer.prototype.maxDelay = 3000;

    MathJaxDelayRenderer.prototype.mathjaxRunning = false;

    MathJaxDelayRenderer.prototype.elapsedTime = 0;

    MathJaxDelayRenderer.prototype.mathjaxDelay = 0;

    MathJaxDelayRenderer.prototype.mathjaxTimeout = void 0;

    bufferId = "mathjax_delay_buffer";

    numBuffers = 0;

    function MathJaxDelayRenderer(params) {
      params = params || {};
      this.maxDelay = params["maxDelay"] || this.maxDelay;
      this.bufferId = params["bufferId"] || (bufferId + numBuffers);
      numBuffers += 1;
      this.$buffer = $("<div>").attr("id", this.bufferId).css("display", "none").appendTo($("body")); // xss-lint: disable=javascript-jquery-insert-into-target
    }


    /*
    render: (params) ->
    params:
      elem: jquery element to be rendered
      text: text to be rendered & put into the element;
        if blank, then just render the current text in the element
      preprocessor: pre-process the text before rendering using MathJax
        if text is blank, it will pre-process the html in the element
      previewSetter: if provided, will pass text back to it instead of
        directly setting the element
     */

    MathJaxDelayRenderer.prototype.render = function(params) {
      var delay, elem, preprocessor, previewSetter, renderer, text;
      elem = params["element"];
      previewSetter = params["previewSetter"];
      text = params["text"];
      if (text == null) {
        text = $(elem).html();
      }
      preprocessor = params["preprocessor"];
      if (params["delay"] === false) {
        if (preprocessor != null) {
          text = preprocessor(text);
        }
        $(elem).html(text); // xss-lint: disable=javascript-jquery-html
        return MathJax.Hub.Queue(["Typeset", MathJax.Hub, $(elem).attr("id")]);
      } else {
        if (this.mathjaxTimeout) {
          window.clearTimeout(this.mathjaxTimeout);
          this.mathjaxTimeout = void 0;
        }
        delay = Math.min(this.elapsedTime + this.mathjaxDelay, this.maxDelay);
        renderer = (function(_this) {
          return function() {
            var curTime, prevTime;
            if (_this.mathjaxRunning) {
              return;
            }
            prevTime = getTime();
            if (preprocessor != null) {
              text = preprocessor(text);
            }
            _this.$buffer.html(text); // xss-lint: disable=javascript-jquery-html
            curTime = getTime();
            _this.elapsedTime = curTime - prevTime;
            if (typeof MathJax !== "undefined" && MathJax !== null) {
              prevTime = getTime();
              _this.mathjaxRunning = true;
              return MathJax.Hub.Queue(["Typeset", MathJax.Hub, _this.$buffer.attr("id")], function() {
                _this.mathjaxRunning = false;
                curTime = getTime();
                _this.mathjaxDelay = curTime - prevTime;
                if (previewSetter) {
                  return previewSetter($(_this.$buffer).html());
                } else {
                  return $(elem).html($(_this.$buffer).html()); // xss-lint: disable=javascript-jquery-html
                }
              });
            } else {
              return _this.mathjaxDelay = 0;
            }
          };
        })(this);
        return this.mathjaxTimeout = window.setTimeout(renderer, delay);
      }
    };

    return MathJaxDelayRenderer;

  })();

}).call(this);
