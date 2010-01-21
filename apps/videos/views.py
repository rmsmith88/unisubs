from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.generic.list_detail import object_list
from videos.forms import VideoForm
from videos.models import Video
import widget

@login_required
def create(request):
    if request.method == 'POST':
        video_form = VideoForm(request.POST)
        if video_form.is_valid():
            video, created = Video.objects.get_or_create(
                                video_url=video_form.cleaned_data.get('video_url'),
                                defaults={'owner': request.user})
            if created:
                # TODO: log to activity feed
                pass
            if video.owner == request.user or video.allow_community_edits:
                return HttpResponseRedirect(reverse(
                        'videos:video', kwargs={'video_id':video.video_id}))
            else:
                # TODO: better error page?
                return HttpResponse('You are not allowed to add transcriptions to this video.')
    else:
        video_form = VideoForm()
    return render_to_response('videos/create.html', locals(),
                              context_instance=RequestContext(request))

@login_required
def video(request, video_id):
    video = get_object_or_404(Video, video_id=video_id)
    video.view_count += 1
    video.save()
    context = widget.js_context(request, video)
    context['video'] = video
    return render_to_response('videos/video.html', context,
                              context_instance=RequestContext(request))
                              
@login_required
def video_list(request):
    try:
        page = int(request.GET['page'])
    except (ValueError, TypeError, KeyError):
        page = 1
    qs = Video.objects.all()
    return object_list(request, queryset=qs, allow_empty=True,
                       paginate_by=50, page=page,
                       template_name='videos/video_list.html',
                       template_object_name='video')
