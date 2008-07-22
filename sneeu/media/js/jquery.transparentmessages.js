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

(function() {
	var _queue = new Array();
	var _visible = false;
	var _element = false;

	function _getTop() {
		var height = window.pageYOffset || document.body.scrollTop || document.documentElement.scrollTop;
		return height + (window.innerHeight - _element.height()) / 2;
	}

	function _create(message) {
		_visible = true;

		if (!_element) {// Initialise
			_element = $('<div class="_tm"></div>')
				.appendTo($('body')[0])
				.css('background', '#000')
				.css('color', '#fff')
				.css('font', '2em sans-serif')
				.css('left', '50%')
				.css('margin', '0 0 0 -10.5em')
				.css('opacity', 0)
				.css('padding', '0.5em')
				.css('position', 'absolute')
				.css('width', '20em');
			$(document).scroll(function() {
				_element.css('top', _getTop());
			});
		}

		_element
			.html(message)
			.css('display', 'block')
			.css('top', _getTop())
			.fadeTo('slow', 0.9, function() {
				setTimeout(function() {// The 'destroy' function
					$(document).bind('mousemove', function() {
						$(document).unbind('mousemove');
						_element.fadeTo('slow', 0, function() {
							_element.css('display', 'none');
							_visible = false;
						});
					});
				}, 2000);
			});
	}

	function _update() {
		if (_visible) {
			setTimeout(function() {
				_update();
			}, 200);
		} else {
			_create(_queue.shift());
		}
	}

	jQuery.message = function(message) {
		_queue.push(message);
		_update();
	}
})();
