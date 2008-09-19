/*
 * Copyright (c) 2008 John Sutherland <john@sneeu.com>
 *
 * Permission to use, copy, modify, and distribute this software for any
 * purpose with or without fee is hereby granted, provided that the above
 * copyright notice and this permission notice appear in all copies.
 *
 * THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
 * WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
 * ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
 * WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
 * ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
 * OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
 */

(function($) {
	function _getTop() {
		var height = window.pageYOffset || document.body.scrollTop || document.documentElement.scrollTop;
		return height + (window.innerHeight - _element.height()) / 2;
	}

	$.fn.scrollOnMousePosition = function() {
		var self = $(this);
		var infoPanel = $('<div id="scrollOnMouseMove_infoPanel"></div>');
		infoPanel.css('height', '320px').css('position', 'fixed').css('top', '50%').css('left', '50%').css('margin', '-160px 0 0 -160px').css('width', '320px').css('opacity', '0.5').css('z-index', '9999').css('background', '#000 url(/media/img/up.png) no-repeat top left');
		infoPanel.addClass('hidden');
		self.append(infoPanel);
		infoPanel.hide();

		var left = self.clientLeft;

		self.css('overflow', 'hidden').css('position', 'relative').css('top', '0px');

		function theScroll(jqElem, n) {
			console.log(n, jqElem.halt);
			if (!jqElem.halt) {
				var newTop = parseInt(jqElem.css('top'));
				// console.log(newTop, newTop + n);
				jqElem.animate({scrollTop: newTop + n}, 100, function() {
					jqElem.halt = false;
					theScroll(jqElem, n);
				});
			 	jqElem.halt = true;
			}
		}

		self.mousemove(function(ev) {
			if (window.innerHeight - ev.clientY < 120) {
				if (infoPanel.hasClass('hidden')) {
					infoPanel.removeClass('hidden');
					infoPanel.fadeIn(200);
				}
				infoPanel.css('background-image', 'url(/media/img/down.png)');
				theScroll(self, 100);
				// while (!infoPanel.hasClass('hidden')) {
					// self.animate({scrollTop: 100});
				// }
			} else if (ev.clientY < 120) {
				if (infoPanel.hasClass('hidden')) {
					infoPanel.removeClass('hidden');
					infoPanel.fadeIn(200);
				}
				infoPanel.css('background-image', 'url(/media/img/up.png)');
				theScroll(self, -100);
				// }
				//ev.clientY / window.innerHeight * self.height() * -1;
			} else {
				self.halt = true;
				infoPanel.fadeOut(200);
				infoPanel.addClass('hidden');
			}
		});
	};
})(jQuery);