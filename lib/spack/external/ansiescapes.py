# MIT License
#
# Copyright (c) 2017 Kodie Grantham
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
import base64
import numbers
import os

ESC = '\u001B['
isTerminalApp = os.environ.get('TERM_PROGRAM') == 'Apple_Terminal'

def _(s): return s.decode('unicode_escape');

def cursorTo(x, y = None):
  if (not isinstance(x, numbers.Number)):
    raise ValueError('The `x` argument is required')

  if not isinstance(y, numbers.Number):
    return _(ESC + str(x + 1) + 'G');

  return _(ESC + str(y + 1) + ';' + str(x + 1) + 'H');

def cursorMove(x, y = None):
  if not isinstance(x, numbers.Number):
    raise ValueError('The `x` argument is required')

  ret = ''

  if x < 0:
    ret += ESC + '-' + str(x) + 'D'
  elif x > 0:
    ret += ESC + str(x) + 'C'

  if y < 0:
    ret += ESC + '-' + str(y) + 'A'
  elif y > 0:
    ret += ESC + str(y) + 'B'

  return _(ret);

def cursorUp(count = 1):
  if not isinstance(count, numbers.Number): count = 1
  return _(ESC + str(count) + 'A');

def cursorDown(count = 1):
  if not isinstance(count, numbers.Number): count = 1
  return _(ESC + str(count) + 'B');

def cursorForward(count = 1):
  if not isinstance(count, numbers.Number): count = 1
  return _(ESC + str(count) + 'C');

def cursorBackward(count = 1):
  if not isinstance(count, numbers.Number): count = 1
  return _(ESC + str(count) + 'D');

cursorLeft = _(ESC + 'G');
cursorSavePosition = _(ESC + ('7' if isTerminalApp else 's'));
cursorRestorePosition = _(ESC + ('8' if isTerminalApp else 'u'));
cursorGetPosition = _(ESC + '6n');
cursorNextLine = _(ESC + 'E');
cursorPrevLine = _(ESC + 'F');
cursorHide = _(ESC + '?25l');
cursorShow = _(ESC + '?25h');

def eraseLines(count = 1):
  clear = ''

  for i in range(count):
    clear += eraseLine + (cursorUp() if i < count - 1 else '')

  return _(clear + cursorLeft);

eraseEndLine = _(ESC + 'K');
eraseStartLine = _(ESC + '1K');
eraseLine = _(ESC + '2K');
eraseDown = _(ESC + 'J');
eraseUp = _(ESC + '1J');
eraseScreen = _(ESC + '2J');
scrollUp = _(ESC + 'S');
scrollDown = _(ESC + 'T');

clearScreen = _('\u001Bc');
beep = _('\u0007');

def image(buf, opts = {}):
  ret = '\u001B]1337;File=inline=1'

  if 'width' in opts:
    ret += ';width=' + str(opts['width'])

  if 'height' in opts:
    ret += ';height=' + str(opts['height'])

  if 'preserveAspectRatio' in opts:
    if (not opts['preserveAspectRatio']):
      ret += ';preserveAspectRatio=0'

  return _(ret + ':' + base64.b64encode(buf) + '\u0007');

def setCwd(cwd = os.getcwd()):
  return _('\u001B]50;CurrentDir=' + cwd + '\u0007');
