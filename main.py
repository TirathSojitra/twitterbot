import tweepy

auth = tweepy.OAuthHandler('Pfgs41tnJrINw8FvOtbKlu3Kq', '26foBJjJ4aolBz8bC15vc3aSt3LOFujSwcWQZRLyF2IahSNk8q')
auth.set_access_token('732211950357123073-z7hZUNtRIpa6sFWJeDGLAr5qoXnuF7M', 'Uwk2jHplQQSh3WPvamFAFpkrVkVzUQupCYXGTDJy8lICc')

api = tweepy.API(auth)

target = api.followers_ids('Gyandu_04')
for i in target:
    user = api.get_user(i)
    print(user.name)
    if user.name == 'Baden Kopp':
        break