import twitter
api = twitter.Api()
sts = api.GetUserTimeline('dhananjayjoshi0')
#print [s.id for s in sts]
k=0
for user2 in sts:
    k=k+1;
    #print user2.user
    print user2.created_at_in_seconds , user2.id
    print user2.created_at  
    print user2.text
    #print user2.user
    print user2.user.time_zone
    print user2.user.profile_link_color
    print user2.user.profile_text_color
    print user2.user.profile_background_color
    print user2.user.lang
    print user2.user.id
    print user2.user.followers_count
    print user2.user.friends_count
    print user2.user.statuses_count
    print user2.user.profile_image_url
    print user2.user.location
    print user2.user.name  
    print user2.user.profile_sidebar_fill_color
    print user2.user.screen_name
    print user2.relative_created_at
    break

