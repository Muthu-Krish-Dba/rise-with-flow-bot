from twikit import Client
import random
import os

QUOTES = [
    "You have to believe in yourself when no one else does. —Serena Williams",
    "When you have a dream, you’ve got to grab it and never let go. —Carol Burnett",
    "Spread love everywhere you go. Let no one ever come without leaving happier. —Mother Teresa",
    "Be yourself; everyone else is already taken. —Oscar Wilde",
    "The biggest adventure you can take is to live the life of your dreams. —Oprah Winfrey",
    "The only thing we have to fear is fear itself. —Franklin D. Roosevelt",
    "Some people want it to happen, some wish it would happen, others make it happen. —Michael Jordan",
    "It does not matter how slowly you go, as long as you do not stop. —Confucius",
    "Find out who you are and do it on purpose. —Dolly Parton",
    "You can be everything. You can be the infinite amount of things that people are. —Kesha",
    "Always go with your passions. Never ask yourself if it’s realistic or not. —Deepak Chopra",
    "Do one thing every day that scares you. —Eleanor Roosevelt",
    "It is never too late to be what you might have been. —George Elliot",
    "Always do your best. What you plant now, you will harvest later. —Og Mandino",
    "Get busy living or get busy dying. —Stephen King",
    "The fear of death follows from the fear of life. A man who lives fully is prepared to die at any time. —Mark Twain",
    "In three words I can sum up everything I’ve learned about life: It goes on. —Robert Frost",
    "You can’t help what you feel, but you can help how you behave. —Margaret Atwood",
    "No need to hurry. No need to sparkle. No need to be anybody but oneself. —Virginia Woolf",
    "It is better to be hated for what you are than to be loved for what you are not. —Andre Gide",
    "Failure is a great teacher and, if you are open to it, every mistake has a lesson to offer. —Oprah Winfrey",
    "If you don’t like the road you’re walking, start paving another one. —Dolly Parton",
    "Keep smiling, because life is a beautiful thing and there’s so much to smile about. —Marilyn Monroe",
    "Be persistent and never give up hope. —George Lucas",
    "There are so many great things in life; why dwell on negativity? —Zendaya",
    "Always remember that you are absolutely unique. Just like everyone else. —Margaret Mead",
    "You don’t always need a plan. Sometimes you just need to breathe, trust, let go and see what happens. —Mandy Hale",
    "Life is like riding a bicycle. To keep your balance, you must keep moving. —Albert Einstein",
    "Nothing is impossible. The word itself says ‘I’m possible!’ —Audrey Hepburn",
    "Life does not have to be perfect to be wonderful. —Annette Funicello"
]

client = Client('en-US')

def login():
    client.login(
        auth_info_1=os.environ["TW_USERNAME"],
        auth_info_2=os.environ["TW_EMAIL"],
        password=os.environ["TW_PASSWORD"]
    )
    client.save_cookies("cookies.json")

def post_tweet():
    quote = random.choice(QUOTES)
    client.load_cookies("cookies.json")
    client.tweet(quote)
    print("Tweet posted:", quote)

if __name__ == "__main__":
    try:
        post_tweet()
    except:
        login()
        post_tweet()
