import twitter
api=twitter.Api(consumer_key='QmnaT4d2f2u6VXTjzkElw',consumer_secret='wZb0CGESCSv1EO5Fc42d7hevNPo7yAFdcs0XZaAe5bE',access_token_key='97845768-fc1dF4oieEknwZFR9YHyA9jklLAdVKO2spdbAQJ3M',access_token_secret='ZSvuI5eyzZLMkCFrfiiEwbpE2kR1WzEazaxdHiJyDxI')
sts=api.GetFriends()
i=0
for user in sts:
   i=i+1
   print 'your friend :', user.name

print 'you have total',i,' friend'

sts1=api.GetFollowers()
j=0
for user1 in sts1:
   j=j+1;
   print 'your FOLLOWER :', user1.name

print 'you have total',j,' friend'

sts2=api.GetReplies()
k=0
for user2 in sts2:
   k=k+1;
   print 'your friend :', user2.text,'message::'

print 'you have total',k,' friend'

m = (i/j)*100+k
print 'YOUR PROFILE RATING IS', m

sts4=api.GetFriends('AshishGadkari')
l=0
for user in sts4:
   l=l+1
   print 'your friend :', user.name

print 'you have total',l,' friend'



