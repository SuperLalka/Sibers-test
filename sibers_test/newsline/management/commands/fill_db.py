# -*- coding: utf-8 -*-
import random
from datetime import datetime
from django.core.management.base import BaseCommand

from newsline.models import News

NEWS_TEXT_EXAMPLES = [
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus vel tristique mauris. "
    "Nulla non quam porttitor, ullamcorper elit a, accumsan purus. Praesent id tempor nisi. "
    "In hac habitasse platea dictumst. Donec et libero sed nisi pharetra auctor ut at lectus. "
    "Nulla dolor purus, auctor condimentum turpis non, ullamcorper ornare orci. "
    "Nulla fringilla lorem velit, vel interdum quam cursus at. Nulla vulputate diam at imperdiet porttitor. "
    "Proin ornare, turpis ut volutpat semper, ex urna dapibus erat, ac tincidunt turpis massa sed odio. "
    "Proin accumsan erat id tempus aliquam. Vestibulum vitae tempus tellus. In finibus auctor aliquam. "
    "Quisque vestibulum eleifend quam, sit amet commodo risus fringilla quis.",
    "Pellentesque risus augue, pharetra cursus sem ac, pellentesque condimentum dui. "
    "Phasellus venenatis urna pretium tortor efficitur pretium. Praesent ut risus hendrerit, pharetra erat non, "
    "porttitor turpis. Curabitur commodo lacinia semper. Etiam magna urna, eleifend vitae euismod id, posuere ac velit. "
    "Donec venenatis eget enim eget scelerisque. Curabitur scelerisque placerat elit, ac scelerisque ipsum ultricies vitae. "
    "In mollis neque a venenatis gravida. Duis eu erat finibus, tristique lorem non, commodo nunc. Maecenas vel rutrum dui. "
    "Maecenas hendrerit mollis velit a suscipit. Duis porttitor nibh metus, quis ornare erat venenatis quis.",
    "Phasellus blandit elit ipsum, nec ultricies magna volutpat et. Phasellus luctus porta mattis. "
    "Cras lorem lectus, aliquet et metus id, ultricies interdum massa. Nunc laoreet dignissim tortor, at pulvinar sem faucibus dictum. "
    "Quisque non lorem eu tellus euismod pulvinar eu in dui. Nam in tortor nulla. Nam libero dui, gravida in mattis vel, "
    "interdum id arcu. Praesent sed erat sit amet nisl sodales malesuada.",
]


class Command(BaseCommand):

    def handle(self, *args, **options):
        news_objects = News.objects.count()
        if news_objects < 60:
            while news_objects < 60:
                news, _ = News.objects.get_or_create(
                    header="HEADER" + " " + str(random.randint(1, 9999)),
                    text=random.choice(NEWS_TEXT_EXAMPLES),
                    type="act"
                )
                news_objects += 1
                print(datetime.now(), f'News {news.id} / {news.header} created')
