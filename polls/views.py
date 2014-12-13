# Create your views here.
from django.shortcuts import render_to_response,get_object_or_404
from django.template import Context,loader
from django.template import RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from polls.models import Poll,Choice
from django.http import Http404
"""
def index(request):
	lastest_poll_list=Poll.objects.all().order_by('-pub_date')[:5]
	return render_to_response('polls/index.html',{'lastest_poll_list':lastest_poll_list})
#	t=loader.get_template('polls/index.html')
#	c=Context({
#			'lastest_poll_list':lastest_poll_list,
#		})
	#output=', '.join([p.question for p in lastest_poll_list])
	#print output
#	return HttpResponse(t.render(c))
"""
"""
def detail(request,poll_id):
	p=get_object_or_404(Poll,pk=poll_id)
#	try:
#		p=Poll.objects.get(pk=poll_id)
#	except Poll.DoesNotExist:
#		raise Http404
	return render_to_response('polls/detail.html',{'poll':p},context_instance=RequestContext(request))
"""

"""
def results(request,poll_id):
	p=get_object_or_404(Poll,pk=poll_id)
	return render_to_response('polls/results.html',{'poll':p})
#	return HttpResponse("You are look at the results of pool %s." % poll_id)
"""

def vote(request,poll_id):
	p=get_object_or_404(Poll,pk=poll_id)
	try:
		selected_choice=p.choice_set.get(pk=request.POST['choice'])
	except (KeyError,Choice.DoesNotExist):
		return render_to_response('polls/detail.html',{'poll':p,'error_message':"You didn't select a choice.",},context_instance=RequestContext(request))
	else:
		selected_choice.votes+=1
		selected_choice.save()
	return HttpResponseRedirect(reverse('poll_results',args=(p.id,)))
#	return HttpResponse("You are voting on poll %s." % poll_id)

