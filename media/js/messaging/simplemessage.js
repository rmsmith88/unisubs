
// Amara, universalsubtitles.org
// 
// Copyright (C) 2012 Participatory Culture Foundation
// 
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU Affero General Public License as
// published by the Free Software Foundation, either version 3 of the
// License, or (at your option) any later version.
// 
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU Affero General Public License for more details.
// 
// You should have received a copy of the GNU Affero General Public License
// along with this program.  If not, see 
// http://www.gnu.org/licenses/agpl-3.0.html.

goog.provide('unisubs.messaging.simplemessage');

unisubs.messaging.simplemessage.MESSAGE_COOKIE_NAME = '_user_message';

unisubs.messaging.simplemessage.showAndRemove = function(messageKey){
    var cookie = new goog.net.Cookies(document);
    var message = cookie.get(messageKey);
    if (message && message.length > 0){
        jQuery['jGrowl'](message, {'life': 10000});
    }
    return cookie.remove(messageKey);
}
 
unisubs.messaging.simplemessage.displayPendingMessages = function(){
    unisubs.messaging.simplemessage.showAndRemove(
        unisubs.messaging.simplemessage.MESSAGE_COOKIE_NAME);
}

goog.exportSymbol(
    "unisubs.messaging.simplemessage.displayPendingMessages",
    unisubs.messaging.simplemessage.displayPendingMessages);
