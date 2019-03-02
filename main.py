# ******************************************************************************
# main.py
#
# Date      Name       Description
# ========  =========  ========================================================
# 3/2/19   Paudel     Initial version,
# ******************************************************************************

from twitter import Twitter
from facebook import Facebook
from linkedin import LinkedIn
from twparser import TwitterParser
from fbparser import FacebookParser
from lkparser import LinkedInParser


def main():
    tw = Twitter()
    tw.call_twitter_api()

    tp = TwitterParser()
    tp.twitter_parser()

    fb = Facebook()
    fb.call_facebook_api()

    fp = FacebookParser()
    fp.facebook_parser()

    lk = LinkedIn()
    lk.call_linkedin_api()

    lp = LinkedInParser()
    lp.linkedin_parser()


if __name__ == '__main__':
    main()