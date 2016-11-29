from django.shortcuts import render, get_object_or_404

from membership.models import CustomSettings, CustomUser


def index(request, user_id=None):

    context = {}
    if user_id:
        # a place to store the end values
        custom_settings = {}

        # get the user's group
        custom_user = get_object_or_404(CustomUser, id=user_id)

        # get the default values
        # see some tips at http://stackoverflow.com/a/844572/4872140
        default_settings = CustomSettings.objects.filter(group__isnull=True,
                                                         user__isnull=True)
        # get the group values
        group_settings = CustomSettings.objects.filter(group=custom_user.group,
                                                       user__isnull=True)
        # get the user values
        user_settings = CustomSettings.objects.filter(group=custom_user.group,
                                                      user=custom_user)
        # probably a more 'pythonic' way to conflate, however:
        # set the values:
        for s in default_settings:
            custom_settings[s.name] = s.value
        for s in group_settings:
            custom_settings[s.name] = s.value
        for s in user_settings:
            custom_settings[s.name] = s.value

        context.update({'custom_user': custom_user,
                        'default_settings': default_settings,
                        'group_settings': group_settings,
                        'user_settings': user_settings,
                        'custom_settings': custom_settings})
        # build
    else:
        context.update({'error': True,
                        'message': 'add /user/1 to the url to get the details for the user. Change the number for the other users'})

    return render(request, 'membership/index.html', context)
