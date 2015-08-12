# Amara, universalsubtitles.org
#
# Copyright (C) 2014 Participatory Culture Foundation
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see
# http://www.gnu.org/licenses/agpl-3.0.html.

"""
SubtitleWorkflow classes for teams
"""

from teams import permissions
from teams.workflows.notes import TeamEditorNotes
import subtitles.workflows

class TeamSubtitlesWorkflow(subtitles.workflows.DefaultWorkflow):
    def __init__(self, team_video):
        subtitles.workflows.DefaultWorkflow.__init__(self, team_video.video)
        self.team_video = team_video
        self.team = team_video.team

    def get_editor_notes(self, language_code):
        return TeamEditorNotes(self.team_video.team, self.team_video.video,
                               language_code)

    def user_can_view_video(self, user):
        return self.team.is_visible or self.team.is_member(user)

    def user_can_view_private_subtitles(self, user, language_code):
        return self.team_video.team.is_member(user)

    def user_can_edit_subtitles(self, user, language_code):
        return permissions.can_add_version(user, self.video, language_code)

class SimpleTeamSubtitlesWorkflow(TeamSubtitlesWorkflow):
    def user_can_edit_subtitles(self, user, language_code):
        return self.team_video.team.is_member(user)