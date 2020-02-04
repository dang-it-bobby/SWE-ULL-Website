def spring_20(request):
    context = {
        # 'upcoming_events': {
        #     'display_title': 'Upcoming Events',
        #     'display_date': 'See Flyer for Dates',
        #     'img_paths': [
        #         'events/img/carousel/fall19/parish/parish_flyer.jpg',
        #     ]
        # },

        'election': {
            'display_title': 'Officer Election',
            'display_date': '4/1/20',
            'display_description': '',
            'img_paths': [
                'events/img/carousel/spring20/election.png',
            ],
            'form_text': 'Officer Application',
            'form_url': 'https://forms.gle/apKxArsi4B11wjNk7'
        },

        'paint': {
            'display_title': 'SWE Square Painting',
            'display_date': '2/8/20',
            'display_description': 'Help us paint the SWE Square. Max 3 people',
            'img_paths': [
                'events/img/carousel/spring20/paint_1.png',
            ],
            'form_text': 'Sign up to volunteer',
            'form_url': 'https://forms.gle/WvVGR3rSURghceaS8'
        },


        '1gm': {
            'display_title': '1st General Meeting',
            'display_date': '2/5/20',
            'display_description': '',
            'img_paths': [
                'events/img/carousel/spring20/1st_gm.png',
            ],
            'form_text': 'Sign up for a chance to win a gift card',
            'form_url': 'https://forms.gle/UQ8uTzKSMqWnm9mM9',

        },


    }

    return context


def fall_19(request):
    context = {
        # 'upcoming_events': {
        #     'display_title': 'Upcoming Events',
        #     'display_date': 'See Flyer for Dates',
        #     'img_paths': [
        #         'events/img/carousel/fall19/parish/parish_flyer.jpg',
        #     ]
        # },

        'we19': {
            'display_title': 'WE19',
            'display_date': '11/7/20 to 11/9/20',
            'display_description': '30 UL Lafayette Students Attended. 25 Total Interviews with 16 Different Companies',
            'img_paths': [
                'events/img/carousel/fall19/we_19/we19_1.JPG',
                'events/img/carousel/fall19/we_19/we19_2.JPG',
            ]
        },

        'parish': {
            'display_title': 'Parish Brewery Tour',
            'display_date': '10/19/20',
            'img_paths': [
                'events/img/carousel/fall19/parish/parish_1.jpg',
                'events/img/carousel/fall19/parish/parish_2.jpg',
                'events/img/carousel/fall19/parish/parish_3.png',
            ]
        },

        'bake_sale_1': {
            'display_title': 'Bake Sale',
            'display_date': '9/20/19',
            'img_paths': [
                'events/img/carousel/fall19/bake_sale_1/bs_1.JPG',
                'events/img/carousel/fall19/bake_sale_1/bs_2.JPG'
            ]
        },

        'meeting_1': {
            'display_title': 'First General Meeting',
            'display_date': '9/11/19',
            'display_description': '',
            'img_paths': [
                'events/img/carousel/fall19/meeting_1/m_5.jpg',
                'events/img/carousel/fall19/meeting_1/m_1.JPG',
                'events/img/carousel/fall19/meeting_1/m_2.JPG',
                'events/img/carousel/fall19/meeting_1/m_3.JPG',
                'events/img/carousel/fall19/meeting_1/m_4.JPG',

            ]
        },

        'les_bbq': {
            'display_title': 'Louisiana Engineering Society BBQ',
            'display_date': '9/6/19',
            'img_paths': [
                'events/img/carousel/fall19/les_bbq/les_bbq_1.JPG',
                'events/img/carousel/fall19/les_bbq/les_bbq_2.JPG',

            ]
        }

    }

    return context
