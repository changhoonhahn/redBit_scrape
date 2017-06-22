import praw 


def scrape_r_Bitcoin(): 
    ''' Using praw scrape the "hot" submissions  
    '''
    reddit = praw.Reddit(user_agent="testing /u/rebbit_scraper",
            client_id='hWy0mOCYtovbSQ', client_secret="toN7hL43GDVjvWleeY95Fzs2UX4",
            username='rebbit_scraper', password='RebbitRebbit')

    for sub in reddit.submission('Bitcoin').hot(limit=100): 

        if '/r/Bitcoin FAQ' in sub.title: 
            print sub.title
            continue
        
        if 'Price Thread' in sub.title: 
            print sub.title
            continue





