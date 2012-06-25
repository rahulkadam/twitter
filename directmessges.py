import twitter
#api=twitter.Api(consumer_key='QmnaT4d2f2u6VXTjzkElw',consumer_secret='wZb0CGESCSv1EO5Fc42d7hevNPo7yAFdcs0XZaAe5bE',access_token_key='97845768-fc1dF4oieEknwZFR9YHyA9jklLAdVKO2spdbAQJ3M',access_token_secret='ZSvuI5eyzZLMkCFrfiiEwbpE2kR1WzEazaxdHiJyDxI')
#sts=api.GetUserTimeline('rahul581')
api1=twitter.Api('rahul581','mission123')
#sts = api.GetUserTimeline()
i=0
print i
for user in sts:
    i=i+1
    print 'your friend :', user.name

print 'you have total',i,' friend'

