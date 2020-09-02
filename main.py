import tweepy
import json

consumer_key: str = 'p8Ikar02jTcyaPNjiKbDFkOZC'
consumer_secret: str = 'kJSHrd9zAL5scnzCeE1Zcpje90EKXNT4rhuYbf2P6UFwUZht3B'
access_token: str = '855639211659198464-WHRyjEZsnV3IiiKqTPXXkkpTx8wWZgb'
access_token_secret: str = 'UpSYJ9GhFsBjhPb0HEpMGy4gl65jjqrrKZTKpWy7PhR5r'

# Funciones para autentificarnos en Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
# Guardamos los 20 tweets del timeline
public_tweets = api.home_timeline()
# Recorremos y mostramos por pantalla


def pp_json(json_thing, sort=True, indents=4):
    if type(json_thing) is str:
        print(json.dumps(json.loads(json_thing), sort_keys=sort, indent=indents))
    else:
        print(json.dumps(json_thing, sort_keys=sort, indent=indents))
    return None


for tweet in public_tweets:
    print('/**************************tweet**************************/')
    pp_json(tweet._json)

user = api.get_user('PandreringPablo')
# Imprime el nombre del usuario por pantalla
print(user.screen_name)
# Imprime el número de seguidores por pantalla
print(user.followers_count)
# Imprime su lista de seguidores
for friend in user.friends():
    print(friend.screen_name)
    friend_chain = api.get_user(friend.screen_name)
    for friend_of_my_friend in friend_chain.friends():
        print('\t')
        print(friend_of_my_friend.screen_name)

