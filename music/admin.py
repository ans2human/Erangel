from django.contrib import admin
from .models import Album, Song
from django.urls import reverse
from django.utils.html import format_html

admin.site.register(Album)

class SongAdmin(admin.ModelAdmin):
	list_display = ['song_title', 'album', 'audio_file', 'is_favorite', 'user_name', 'link_to_user']


	def link_to_user(self, obj):

	    link = reverse("admin:auth_user_change", args=[obj.album.user.id])

	    return format_html('<a href="{}"> {}</a>', link, obj.album.user.id)

	link_to_user.short_description = 'UserID'


	# def link_to_username(self, obj):
	# 	link = reverse("admin:music_song_change", args=[obj.Song.user_name])
	# 	return u'<a href="%s">%s</a>' % (link,obj.Song.user_name)
	# link_to_username.allow_tags=True


admin.site.register(Song,SongAdmin)
