# -*- coding: utf-8 -*-
"""Shared content data for Orlando Water Pros."""

# ---------------------------------------------------------------- site config
SITE = {
        'brand': 'Orlando Water Pros',
        'region': 'Central Florida',
        'legal': 'Orlando Water Pros',
        'email': 'hello@orlandowaterpros.com',
        'hours': 'Mon–Fri 8am–6pm · Sat 9am–2pm',
        # Same hours as above, structured for schema.org. Keep the two in sync.
        'hours_spec': [
            (['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'], '08:00', '18:00'),
            (['Saturday'], '09:00', '14:00'),
        ],
        # Canonical host. The site is served at www; the apex redirects to it.
        # This must match the host that actually serves the pages, or every
        # canonical/og:url tag points somewhere else.
        'domain': 'www.orlandowaterpros.com',
        'phone_display': '(689) 210-3180',
        'phone_href': '+16892103180',

        # --- GoHighLevel chat widget -------------------------------------
        # Temporary, installed for GHL's A2P 10DLC verification.
        # Set chat_widget to False and rebuild to remove it from every page.
        'chat_widget': False,
        'chat_widget_id': '6aa4cb10316a723a13d93bef',

        # Quote/contact forms stay OFF while the GHL chat widget is up.
        # A2P 10DLC: Everett attested to the carriers that the chat widget is
        # the ONLY thing on the site collecting phone numbers for SMS opt-in.
        # A visible quote form with a consent checkbox breaks that attestation.
        # Flip this to True only when the widget comes down.
        'show_forms': True,

        # --- Where the quote form sends leads ----------------------------
        # A GoHighLevel Inbound Webhook URL (Workflows -> new workflow ->
        # trigger "Inbound Webhook" -> copy the URL). The form POSTs JSON
        # with first_name, last_name, phone, email, zip, best_time, message,
        # sms_consent, page and submitted_at.
        # While this is empty the form falls back to opening the visitor's
        # mail app pre-filled, so no lead is silently dropped.
        'form_endpoint': 'https://services.leadconnectorhq.com/hooks/f3sx3bB5dnapd0kKjANK/webhook-trigger/6a3ad9d3-8d9f-4158-b56b-f11429b34aa8'
    }

# ---------------------------------------------------------------- service area
# Each city carries its real EWG Tap Water Database figures, pulled from the
# utility that actually serves it. Re-check these when EWG refreshes the data.
CITIES = [
        {
            'slug': 'orlando',
            'name': 'Orlando',
            'county': 'Orange County',
            'hard': '7',
            'supply': 'OUC (Lower Floridan Aquifer)',
            'note': "OUC draws Orlando's water from the Lower Floridan Aquifer and treats it with ozone, which lets it use less chlorine. It doesn't use chloramine. OUC's published average hardness is 7 grains per gallon (129 ppm), right on the line where water counts as hard.",
            'issues': [
                'Chlorine taste and odor',
                'Scale on fixtures and glassware',
                'Spotting on dishes and shower doors'
            ],
            'ewg': {
                'utility': 'Orlando Utilities Commission',
                'url': 'https://www.ewg.org/tapwater/system.php?pws=FL3480962',
                'total': 16,
                'over': 7,
                'top': [
                    ('Haloacetic acids (HAA9)', '32.7 ppb', '0.06 ppb', '544x', 'cancer'),
                    ('Total trihalomethanes (TTHMs)', '53.4 ppb', '0.15 ppb', '356x', 'cancer'),
                    ('Haloacetic acids (HAA5)', '23.8 ppb', '0.1 ppb', '238x', 'cancer'),
                    ('Bromate', '3.52 ppb', '0.1 ppb', '35x', 'cancer')
                ]
            }
        },
        {
            'slug': 'winter-park',
            'name': 'Winter Park',
            'county': 'Orange County',
            'hard': '10–15',
            'supply': 'City of Winter Park utility',
            'note': 'Winter Park runs hard, consistently. Older homes here often carry a decade of scale in the water heater before anyone installs treatment.',
            'issues': [
                'Hard water scale',
                'Water heaters failing early',
                'Spotting on fixtures'
            ],
            'ewg': {
                'utility': 'City of Winter Park',
                'url': 'https://www.ewg.org/tapwater/system.php?pws=FL3481482',
                'total': 16,
                'over': 5,
                'top': [
                    ('Haloacetic acids (HAA9)', '35.9 ppb', '0.06 ppb', '599x', 'cancer'),
                    ('Total trihalomethanes (TTHMs)', '64.4 ppb', '0.15 ppb', '429x', 'cancer'),
                    ('Haloacetic acids (HAA5)', '24.1 ppb', '0.1 ppb', '241x', 'cancer'),
                    ('Bromate', '4.28 ppb', '0.1 ppb', '43x', 'cancer')
                ]
            }
        },
        {
            'slug': 'kissimmee',
            'name': 'Kissimmee',
            'county': 'Osceola County',
            'hard': '12–18',
            'supply': 'Toho Water Authority',
            'note': 'Osceola runs harder than Orlando. Sulfur odor is a common complaint across the county, and it gets worse on private wells.',
            'issues': [
                'High hardness',
                'Sulfur (rotten-egg) odor',
                'Appliance scale'
            ],
            'ewg': {
                'utility': 'Toho Water Authority',
                'url': 'https://www.ewg.org/tapwater/system.php?pws=FL3490751',
                'total': 11,
                'over': 3,
                'top': [
                    ('Haloacetic acids (HAA9)', '32.9 ppb', '0.06 ppb', '548x', 'cancer'),
                    ('Total trihalomethanes (TTHMs)', '49.3 ppb', '0.15 ppb', '328x', 'cancer'),
                    ('Haloacetic acids (HAA5)', '29.3 ppb', '0.1 ppb', '293x', 'cancer')
                ]
            }
        },
        {
            'slug': 'st-cloud',
            'name': 'St. Cloud',
            'county': 'Osceola County',
            'hard': '12–18',
            'supply': 'Toho Water Authority (runs the city system)',
            'note': 'Same aquifer conditions as the rest of Osceola: hard water everywhere, plus a large number of homes on private wells fighting iron and sulfur.',
            'issues': [
                'High hardness',
                'Iron staining on wells',
                'Sulfur odor'
            ],
            'ewg': {
                'utility': 'City of St. Cloud',
                'url': 'https://www.ewg.org/tapwater/system.php?pws=FL3491373',
                'total': 11,
                'over': 5,
                'top': [
                    ('Haloacetic acids (HAA9)', '23.6 ppb', '0.06 ppb', '394x', 'cancer'),
                    ('Total trihalomethanes (TTHMs)', '48.7 ppb', '0.15 ppb', '325x', 'cancer'),
                    ('Haloacetic acids (HAA5)', '32.0 ppb', '0.1 ppb', '320x', 'cancer'),
                    ('Radium, combined', '0.64 pCi/L', '0.05 pCi/L', '13x', 'cancer')
                ]
            }
        },
        {
            'slug': 'clermont',
            'name': 'Clermont',
            'county': 'Lake County',
            'hard': '15–25',
            'supply': 'City of Clermont utility & private wells',
            'note': 'Lake County has the hardest water in Central Florida, and Clermont sits at the top of the range. Most homes outside city limits are on wells.',
            'issues': [
                'Very high hardness',
                'Iron and sulfur on wells',
                'Fast scale buildup'
            ],
            'ewg': {
                'utility': 'City of Clermont',
                'url': 'https://www.ewg.org/tapwater/system.php?pws=FL3350215',
                'total': 23,
                'over': 11,
                'top': [
                    ('Haloacetic acids (HAA9)', '13.6 ppb', '0.06 ppb', '226x', 'cancer'),
                    ('Haloacetic acids (HAA5)', '15.4 ppb', '0.1 ppb', '154x', 'cancer'),
                    ('Total trihalomethanes (TTHMs)', '17.7 ppb', '0.15 ppb', '118x', 'cancer'),
                    ('Bromodichloromethane', '5.16 ppb', '0.06 ppb', '86x', 'cancer')
                ]
            }
        },
        {
            'slug': 'lake-mary',
            'name': 'Lake Mary',
            'county': 'Seminole County',
            'hard': '10–16',
            'supply': 'City of Lake Mary utility',
            'note': 'Seminole County runs hard across the board. Most Lake Mary homes want softening plus carbon filtration for taste.',
            'issues': [
                'Hard water scale',
                'Chlorine taste',
                'Dry skin and hair'
            ],
            'ewg': {
                'utility': 'City of Lake Mary',
                'url': 'https://www.ewg.org/tapwater/system.php?pws=FL3590201',
                'total': 19,
                'over': 4,
                'top': [
                    ('PFHxS (forever chemical)', '1.80 ppt', '0.001 ppt', '1,800x', ''),
                    ('Haloacetic acids (HAA9)', '17.9 ppb', '0.06 ppb', '299x', 'cancer'),
                    ('Total trihalomethanes (TTHMs)', '24.5 ppb', '0.15 ppb', '163x', 'cancer'),
                    ('Haloacetic acids (HAA5)', '6.53 ppb', '0.1 ppb', '65x', 'cancer')
                ]
            }
        },
        {
            'slug': 'sanford',
            'name': 'Sanford',
            'county': 'Seminole County',
            'hard': '10–16',
            'supply': 'City of Sanford utility',
            'note': 'Sanford draws from the Floridan Aquifer and lands squarely in the hard range. Older parts of town report sulfur odor now and then.',
            'issues': [
                'Hard water scale',
                'Occasional sulfur odor',
                'Fixture spotting'
            ],
            'ewg': {
                'utility': 'City of Sanford',
                'url': 'https://www.ewg.org/tapwater/system.php?pws=FL3590205',
                'total': 19,
                'over': 6,
                'top': [
                    ('PFHxS (forever chemical)', '1.53 ppt', '0.001 ppt', '1,525x', ''),
                    ('Haloacetic acids (HAA9)', '30.3 ppb', '0.06 ppb', '505x', 'cancer'),
                    ('Total trihalomethanes (TTHMs)', '60.2 ppb', '0.15 ppb', '401x', 'cancer'),
                    ('Haloacetic acids (HAA5)', '18.1 ppb', '0.1 ppb', '181x', 'cancer')
                ]
            }
        },
        {
            'slug': 'altamonte-springs',
            'name': 'Altamonte Springs',
            'county': 'Seminole County',
            'hard': '10–16',
            'supply': 'City of Altamonte Springs utility',
            'note': 'Standard Seminole County water. Hard enough that scale shows on the shower door and inside the water heater within a few years.',
            'issues': [
                'Hard water scale',
                'Soap scum',
                'Chlorine taste'
            ],
            'ewg': {
                'utility': 'Altamonte Springs Water Department',
                'url': 'https://www.ewg.org/tapwater/system.php?pws=FL3590026',
                'total': 14,
                'over': 4,
                'top': [
                    ('PFHxS (forever chemical)', '0.950 ppt', '0.001 ppt', '950x', ''),
                    ('Haloacetic acids (HAA9)', '29.3 ppb', '0.06 ppb', '488x', 'cancer'),
                    ('Total trihalomethanes (TTHMs)', '44.1 ppb', '0.15 ppb', '294x', 'cancer'),
                    ('Haloacetic acids (HAA5)', '22.4 ppb', '0.1 ppb', '224x', 'cancer')
                ]
            }
        },
        {
            'slug': 'oviedo',
            'name': 'Oviedo',
            'county': 'Seminole County',
            'hard': '10–16',
            'supply': 'City of Oviedo utility',
            'note': 'Typical Seminole hardness. Newer subdivisions come plumbed with a softener loop in the garage, which makes install day short.',
            'issues': [
                'Hard water scale',
                'Spotting on glassware',
                'Chlorine taste'
            ],
            'ewg': {
                'utility': 'City of Oviedo',
                'url': 'https://www.ewg.org/tapwater/system.php?pws=FL3590970',
                'total': 12,
                'over': 4,
                'top': [
                    ('Haloacetic acids (HAA9)', '11.2 ppb', '0.06 ppb', '187x', 'cancer'),
                    ('Total trihalomethanes (TTHMs)', '19.6 ppb', '0.15 ppb', '130x', 'cancer'),
                    ('Haloacetic acids (HAA5)', '11.4 ppb', '0.1 ppb', '114x', 'cancer'),
                    ('Radium, combined', '0.73 pCi/L', '0.05 pCi/L', '15x', 'cancer')
                ]
            }
        },
        {
            'slug': 'apopka',
            'name': 'Apopka',
            'county': 'Orange County',
            'hard': '6–13',
            'supply': 'City of Apopka utility & private wells',
            'note': "The City of Apopka puts its source water at 102 to 222 ppm of hardness, or 6 to 13 grains per gallon. The rural areas around it are dense with private wells carrying iron and hydrogen sulfide.",
            'issues': [
                'High hardness',
                'Iron staining',
                'Sulfur odor on wells'
            ],
            'ewg': {
                'utility': 'City of Apopka',
                'url': 'https://www.ewg.org/tapwater/system.php?pws=FL3480200',
                'total': 16,
                'over': 7,
                'top': [
                    ('Haloacetic acids (HAA9)', '29.5 ppb', '0.06 ppb', '492x', 'cancer'),
                    ('Total trihalomethanes (TTHMs)', '45.7 ppb', '0.15 ppb', '304x', 'cancer'),
                    ('Haloacetic acids (HAA5)', '23.2 ppb', '0.1 ppb', '232x', 'cancer'),
                    ('Arsenic', '0.140 ppb', '0.004 ppb', '35x', 'cancer')
                ]
            }
        },
        {
            'slug': 'winter-garden',
            'name': 'Winter Garden',
            'county': 'Orange County',
            'hard': '12–18',
            'supply': 'City of Winter Garden & Orange County Utilities',
            'note': 'West Orange County water sits on the harder end. Owners in the newer neighborhoods usually call after spotting scale on fixtures that are barely a year old.',
            'issues': [
                'High hardness',
                'Scale on new fixtures',
                'Appliance wear'
            ],
            'ewg': {
                'utility': 'Winter Garden Water Department',
                'url': 'https://www.ewg.org/tapwater/system.php?pws=FL3481481',
                'total': 17,
                'over': 7,
                'top': [
                    ('Haloacetic acids (HAA9)', '14.5 ppb', '0.06 ppb', '241x', 'cancer'),
                    ('Total trihalomethanes (TTHMs)', '23.0 ppb', '0.15 ppb', '154x', 'cancer'),
                    ('Haloacetic acids (HAA5)', '8.67 ppb', '0.1 ppb', '87x', 'cancer'),
                    ('Arsenic', '0.300 ppb', '0.004 ppb', '75x', 'cancer')
                ]
            }
        },
        {
            'slug': 'ocoee',
            'name': 'Ocoee',
            'county': 'Orange County',
            'hard': '12–18',
            'supply': 'City of Ocoee utility',
            'note': "Ocoee shares West Orange County's harder supply. A softener paired with carbon filtration is the usual answer here.",
            'issues': [
                'High hardness',
                'Chlorine taste and odor',
                'Soap scum'
            ],
            'ewg': {
                'utility': 'City of Ocoee',
                'url': 'https://www.ewg.org/tapwater/system.php?pws=FL3480204',
                'total': 21,
                'over': 8,
                'top': [
                    ('PFHxS (forever chemical)', '1.000 ppt', '0.001 ppt', '1,000x', ''),
                    ('Haloacetic acids (HAA9)', '30.7 ppb', '0.06 ppb', '511x', 'cancer'),
                    ('Total trihalomethanes (TTHMs)', '36.2 ppb', '0.15 ppb', '242x', 'cancer'),
                    ('Haloacetic acids (HAA5)', '19.5 ppb', '0.1 ppb', '195x', 'cancer')
                ]
            }
        },
        {
            'slug': 'windermere',
            'name': 'Windermere',
            'county': 'Orange County',
            'hard': '10–16',
            'supply': 'Orange County Utilities & private wells',
            'note': 'A mix of municipal service and private wells. The larger homes here need higher-capacity equipment to keep up with the fixture count.',
            'issues': [
                'Hard water scale',
                'Well iron and sulfur',
                'High household demand'
            ],
            'ewg': {
                'utility': 'Orange County Utilities — South',
                'url': 'https://www.ewg.org/tapwater/system.php?pws=FL3484119',
                'total': 29,
                'over': 12,
                'top': [
                    ('Haloacetic acids (HAA9)', '46.2 ppb', '0.06 ppb', '770x', 'cancer'),
                    ('Total trihalomethanes (TTHMs)', '54.7 ppb', '0.15 ppb', '365x', 'cancer'),
                    ('Haloacetic acids (HAA5)', '25.1 ppb', '0.1 ppb', '251x', 'cancer'),
                    ('Bromodichloromethane', '14.2 ppb', '0.06 ppb', '236x', 'cancer')
                ]
            }
        },
        {
            'slug': 'deltona',
            'name': 'Deltona',
            'county': 'Volusia County',
            'hard': '12–18',
            'supply': 'City of Deltona utility & private wells',
            'note': "Deltona has more private wells than anywhere else we serve. That's where the iron staining and sulfur odor show up.",
            'issues': [
                'Iron staining',
                'Sulfur odor',
                'High hardness'
            ],
            'ewg': {
                'utility': 'Deltona Water',
                'url': 'https://www.ewg.org/tapwater/system.php?pws=FL3640287',
                'total': 23,
                'over': 10,
                'top': [
                    ('PFHxS (forever chemical)', '1.93 ppt', '0.001 ppt', '1,929x', ''),
                    ('Haloacetic acids (HAA9)', '24.6 ppb', '0.06 ppb', '409x', 'cancer'),
                    ('Haloacetic acids (HAA5)', '23.7 ppb', '0.1 ppb', '237x', 'cancer'),
                    ('Total trihalomethanes (TTHMs)', '28.5 ppb', '0.15 ppb', '190x', 'cancer')
                ]
            }
        }
    ]

# Per-city extras, all checked against the utility's own documents in Nov 2026.
#   geo        approximate city centre, used only to order "nearby areas"; never shown
#   report_url the utility's water quality report page (None = none found online)
#   facts      plain restatements of the utility's own wording, from facts_src.
#              Never add a fact here without a primary source in facts_src.
#   hard_src   set only where the hardness figure itself is published by the
#              utility; every other city's 'hard' range is UNSOURCED (see CLAUDE.md)
CITY_LOCAL = {
    'orlando': {
        'geo': (28.538, -81.379), 'report_by': 'Orlando Utilities Commission (OUC)',
        'report_url': 'https://www.ouc.com/about-ouc/company-publications/water-quality-reports',
        'hard_src': ('OUC', 'https://www.ouc.com/environment-community/high-quality-water-ouc'),
        'facts': [
            "Water comes from the Lower Floridan Aquifer.",
            "OUC uses ozone treatment to remove tastes and odors, which lets it use less chlorine.",
            "Chlorine averages 1.0 ppm. OUC does not use chloramine.",
            "Average hardness is 129 ppm, or 7 grains per gallon.",
        ],
        'facts_src': ('OUC water services page', 'https://www.ouc.com/environment-community/high-quality-water-ouc'),
    },
    'winter-park': {
        'geo': (28.600, -81.339), 'report_by': 'the City of Winter Park',
        'report_url': 'https://cityofwinterpark.org/departments/water-wastewater-utilities/water-treatment',
        'facts': [
            "Drinking water comes from four interconnected water plants.",
            "Treatment includes chlorination, ozonation, and sodium hydroxide for corrosion control.",
        ],
        'facts_src': ('City of Winter Park water treatment page',
                      'https://cityofwinterpark.org/departments/water-wastewater-utilities/water-treatment'),
    },
    'kissimmee': {
        'geo': (28.292, -81.408), 'report_by': 'Toho Water Authority',
        'report_url': 'https://www.tohowater.com/waterquality',
        'facts': [
            "Toho publishes separate water quality reports for five service areas: Central, Eastern, "
            "Southern, St. Cloud and Western. Check which one covers your address.",
        ],
        'facts_src': ('Toho Water Authority water quality page', 'https://www.tohowater.com/waterquality'),
    },
    'st-cloud': {
        'geo': (28.249, -81.281), 'report_by': 'Toho Water Authority',
        'report_url': 'https://www.tohowater.com/waterquality',
        'facts': [
            "Toho Water Authority took over management and operation of St. Cloud's water utility in "
            "October 2022. The agreement was not a sale of the utility.",
            "Toho publishes a dedicated St. Cloud water quality report.",
        ],
        'facts_src': ('Around Osceola, Feb 2022',
                      'https://www.aroundosceola.com/news/toho-water-assume-management-st-cloud-water-utility'),
    },
    'clermont': {
        'geo': (28.549, -81.773), 'report_by': 'the City of Clermont',
        'report_url': 'https://www.clermontfl.gov/Archive.aspx?AMID=37',
        'facts': [
            "Water comes from the Floridan Aquifer through eight city wells with a combined capacity of "
            "12 million gallons per day.",
            "The city describes its groundwater as typically high quality, needing only chlorine disinfection.",
        ],
        'facts_src': ('City of Clermont water page', 'https://www.clermontfl.gov/201/Water-Wastewater'),
    },
    'lake-mary': {
        'geo': (28.759, -81.318), 'report_by': 'the City of Lake Mary',
        'report_url': 'https://www.lakemaryfl.com/341/Water-Quality',
        'facts': [
            "Six groundwater wells draw from the upper Floridan Aquifer.",
            "Treatment includes an ultraviolet advanced oxidation process, granular activated carbon and "
            "chlorination.",
            "The city's lead service line inventory found no lead service lines.",
        ],
        'facts_src': ('Lake Mary 2025 water quality report', 'https://www.lakemaryfl.com/342/2025-Water-Quality-Report'),
    },
    'sanford': {
        'geo': (28.800, -81.273), 'report_by': 'the City of Sanford',
        'report_url': 'https://sanfordfl.gov/wp-content/uploads/2026/04/City-of-Sanford-Annual-Water-Quality-Report-2026.pdf',
        'facts': [
            "Seventeen groundwater wells draw from the Floridan Aquifer: thirteen supply the Main Water Plant "
            "and four the Auxiliary Water Plant.",
            "Water is chlorinated for disinfection, and polyphosphate is added for corrosion control.",
        ],
        'facts_src': ('Sanford water quality report (2025 data)',
                      'https://sanfordfl.gov/wp-content/uploads/2026/04/City-of-Sanford-Annual-Water-Quality-Report-2026.pdf'),
    },
    'altamonte-springs': {
        'geo': (28.661, -81.366), 'report_by': 'the City of Altamonte Springs',
        'report_url': 'https://www.altamonte.org/1271/Water-Quality',
        'facts': [
            "Water is groundwater from the Floridan Aquifer, pumped from six city wells.",
            "Treatment includes tray aeration to remove hydrogen sulfide, chlorination for disinfection, and "
            "orthophosphate for corrosion control.",
        ],
        'facts_src': ('Altamonte Springs water quality report (2025 data)',
                      'https://www.altamonte.org/DocumentCenter/View/10009/2024-Annual-Drinking-Water-Quality-Report'),
    },
    'oviedo': {
        'geo': (28.670, -81.208), 'report_by': 'the City of Oviedo',
        'report_url': 'https://cityofoviedo.net/1206/Water',
        'facts': [
            "Ten wells draw from the Floridan Aquifer.",
            "Treatment is forced-draft aeration and chloramine disinfection.",
            "Testing showed no detectable quantities of any of the 29 PFAS compounds tested.",
        ],
        'facts_src': ('Oviedo 2024 drinking water quality report',
                      'https://cityofoviedo.net/DocumentCenter/View/9020/2024-Water-Quality-Drinking-Report'),
    },
    'apopka': {
        'geo': (28.676, -81.512), 'report_by': 'the City of Apopka', 'report_url': None,
        'hard_src': ('City of Apopka', 'https://www.apopka.net/Faq.aspx?QID=158'),
        'facts': [
            "The city puts its source water at 102 to 222 ppm of hardness, which it equates to 6 to 13 "
            "grains per gallon.",
        ],
        'facts_src': ('City of Apopka water FAQ', 'https://www.apopka.net/Faq.aspx?QID=158'),
    },
    'winter-garden': {
        'geo': (28.565, -81.586), 'report_by': 'the City of Winter Garden',
        'report_url': 'https://wgfl.gov/454/Water-Quality-Report',
        'facts': [
            "Six deep wells draw from the Floridan Aquifer.",
            "Treatment is aeration and disinfection with sodium hypochlorite (chlorine).",
        ],
        'facts_src': ('Winter Garden 2024 water quality report',
                      'https://www.cwgdn.com/DocumentCenter/View/7004/Water-Quality-Report-2024'),
    },
    'ocoee': {
        'geo': (28.569, -81.544), 'report_by': 'the City of Ocoee',
        'report_url': 'https://www.ocoee.org/ccr',
        'facts': [
            "Groundwater is drawn from the Floridan Aquifer at depths of 340 to 1,450 feet.",
            "Water is chlorinated for disinfection.",
            "The Forest Lake Estates service area gets its water from Orange County Utilities.",
            "The city's 2024 service line inventory found no lead service lines.",
        ],
        'facts_src': ('Ocoee 2024 water quality report', 'https://www.ocoee.org/Archive.aspx?ADID=1789'),
    },
    'windermere': {
        'geo': (28.496, -81.535), 'report_by': 'Orange County Utilities',
        'report_url': 'https://www.ocfl.net/WaterQuality',
        # Town of Windermere runs no water system of its own; its site
        # sends water questions to Orange County Utilities.
        'supply_answer': ("The Town of Windermere doesn't run its own water system. "
                          "Homes are either connected to Orange County Utilities or on a private well."),
        'facts': [
            "Orange County Utilities draws from the Floridan Aquifer.",
            "The county says its groundwater needs little treatment beyond disinfection and aeration to "
            "remove naturally present hydrogen sulfide.",
            "Its service line inventory found no lead service lines.",
        ],
        'facts_src': ('Orange County Utilities 2025 drinking water report',
                      'https://www.ocfl.net/Portals/0/Library/Water-Garbage-Recycle/docs/AnnualDrinkingWaterReport2025-OCU.pdf'),
    },
    'deltona': {
        'geo': (28.900, -81.264), 'report_by': 'the City of Deltona',
        'report_url': 'https://www.deltonafl.gov/DocumentCenter/View/1711',
        'facts': [
            "Water is groundwater from the Floridan Aquifer.",
            "Treatment includes aeration, chloramine disinfection (chlorine plus ammonia), and a "
            "phosphate-based corrosion control chemical.",
        ],
        'facts_src': ('Deltona 2024 water quality report', 'https://www.deltonafl.gov/DocumentCenter/View/1711'),
    },
}

# ---------------------------------------------------------------- products
PRODUCTS = [
        {
            'slug': 'softener-carbon-filtration',
            'name': 'Softener + Carbon Filtration',
            'cat': 'Whole Home',
            'tag': 'Most Popular',
            'img': 'softener-carbon-filtration.webp',
            'photo': 'Single-tank softener with carbon',
            'short': 'One tank, two jobs. Softening resin and carbon in a single unit for the two most common city water problems.',
            'who': 'Homes wanting softened, better-tasting water without room for a two-tank setup.',
            'bullets': [
                'Combined softening resin and coconut shell carbon in one tank',
                'Removes hardness plus chlorine taste and odor',
                'Smaller footprint than a dual-tank system',
                'Salt-efficient regeneration',
                'Polishing gravel bed prevents channeling',
                'Digital control valve with memory backup'
            ],
            'long': [
                'Hardness and chlorine are the two things almost every Central Florida city-water home is dealing with. This system handles both in one tank, which matters when the water heater closet is the only place a system can go.',
                'The mixed bed layers high-capacity softening resin over coconut shell carbon, with polishing gravel underneath to keep water distributing evenly instead of channeling down one side. You get soft water and chlorine removal from a single unit on a single service schedule.',
                'The trade-off against a dual-tank system is media volume — one tank holds less of each medium than two dedicated tanks. For most homes that difference never shows up in daily use, and the space saved is worth more.'
            ]
        },
        {
            'slug': 'city-water-dual-tank',
            'name': 'City Water Dual Tank',
            'cat': 'Whole Home',
            'img': 'city-water-dual-tank.webp',
            'photo': 'Two-tank city water system',
            'short': 'Two dedicated tanks for city water — one for filtration, one for softening. Each job gets its own media bed.',
            'who': 'City-water homes that want the strongest whole-home treatment we install.',
            'bullets': [
                'Separate carbon tank removes chlorine, chloramine and sediment',
                'Separate softener tank removes calcium and magnesium hardness',
                'Each media bed sized and serviced independently',
                'WQA Gold Seal CG10 softening resin',
                'Programmable digital control valve',
                'Most media volume of any system we install'
            ],
            'long': [
                'Splitting filtration and softening across two tanks means neither job is a compromise. The first tank is a dedicated carbon bed that strips chlorine, chloramine and sediment before the water reaches anything else. The second is a full softener that handles hardness on its own.',
                'The practical advantage shows up over time. Chlorine is what degrades softening resin, so removing it upstream extends the life of the resin bed considerably. It also means each tank can be serviced on its own schedule rather than replacing a combined bed when only half of it is spent.',
                'This is the configuration we recommend when a home is on city water and wants whole-home treatment that will still be performing well in a decade.'
            ]
        },
        {
            'slug': 'well-water-dual-tank',
            'name': 'Well Water Dual Tank',
            'cat': 'Well Water',
            'img': 'well-water-dual-tank.webp',
            'photo': 'Dual-tank well water system',
            'short': 'Complete well water treatment in two tanks — iron and sediment removal on one side, softening on the other.',
            'who': 'Wells dealing with iron staining, sediment and hardness together.',
            'bullets': [
                'Dedicated iron and sediment removal tank',
                'Dedicated softening tank with WQA Gold Seal CG10 resin',
                'Handles staining, hardness and grit in one system',
                'Built for well water chemistry rather than adapted from a city system',
                'Backwashing media beds, no cartridge changes',
                'Digital control valve on each tank'
            ],
            'long': [
                'Where a well has iron and hardness but not a significant sulfur problem, a dual-tank setup is the right fit. It costs less than a chemical injection setup, takes up less space, and there is no chemical to keep topped up.',
                'The first tank removes iron and sediment, protecting everything downstream from staining and abrasion. The second is a dedicated softener running WQA Gold Seal resin that handles hardness on its own bed and its own schedule.',
                'If a lab panel comes back showing significant hydrogen sulfide as well, we will tell you plainly that this system is not the right one and talk you through what is. Sizing a well system off a guess is how people end up replacing equipment twice.'
            ]
        }

    ]

PRODUCT_CATS = [
        'Whole Home',
        'Well Water'
    ]

# ------------------------------------------- manufacturer-published specs
SPECS = {
        'softener-carbon-filtration': [
            ('Tanks', 'Single mixed-media tank'),
            ('Media', 'High-capacity softening resin, coconut shell carbon, polishing gravel'),
            ('Targets', 'Hardness (calcium & magnesium), chlorine taste and odor'),
            ('Brine tank', '15" x 35" square')
        ],
        'city-water-dual-tank': [
            ('Tanks', 'Two \u2014 dedicated carbon and dedicated softener'),
            ('Media', 'CG10 softening resin, granular activated coconut shell carbon'),
            ('Resin', 'WQA Gold Seal award-winning resin'),
            ('Targets', 'Hardness, chlorine, chloramine, sediment'),
            ('Bypass size', '1"')
        ],
        'well-water-dual-tank': [
            ('Tanks', 'Two \u2014 iron/sediment removal and softening'),
            ('Media', 'CG10 softening resin, granular activated coconut shell carbon, Katalox Light'),
            ('Resin', 'WQA Gold Seal award-winning resin'),
            ('Targets', 'Iron, sediment, hardness'),
            ('Bypass size', '1"')
        ]
    }

# ---------------------------------------------------------------- comparison
COMPARE_COLS = [
        'Orlando Water Pros',
        'Culligan',
        'Kinetico',
        'Leaf Water',
        'Home Depot DIY'
    ]

COMPARE_ROWS = [
        ('Installed by the company you hired', 'yes', 'Varies', 'Varies', 'Varies', 'no:DIY'),
        ('Lifetime limited warranty', 'yes', '1 year', '10 year', '1 year', 'no'),
        ('No long-term contracts', 'yes', 'Multi-year typical', 'Multi-year typical', 'Multi-year typical', 'N/A'),
        ('Transparent pricing', 'yes', 'no', 'no', 'no', 'yes'),
        ('Same-week installation', 'yes', '2–3 weeks', '2–3 weeks', '2–3 weeks', 'DIY timeline')
    ]

# ---------------------------------------------------------------- maintenance
MAINTENANCE = [
        ('Salt refill', '1–2 bags every 4–6 weeks', 'You buy it — about $6–8 a bag', 'Every system we install'),
        ('Softening resin', 'Swap every 7–12 years', '', 'Every system we install'),
        ('Carbon media', '10+ years', '', 'Every system we install'),
        ('Backwash cycle', 'Automatic, set at install', 'No cost — no cartridges to swap', 'Every system we install')
    ]

# ---------------------------------------------------------------- credentials
CERTS = [
        ('NSF-Certified Components', 'The carbon media, gravel, holding tanks and main valves in our systems carry NSF certification, including carbon from Jacobi Carbons.'),
        ('Drinking Water System Components', 'Our components are certified under the NSF Drinking Water System Components program, the standard covering everything your water actually touches.'),
        ('Cation Exchange Water Softeners', 'Our softeners are certified under the NSF program for cation exchange water softeners, the category that covers ion-exchange performance.'),
        ('WQA Gold Seal', 'Water Quality Association Gold Seal certification, held on top of NSF certification. Two independent bodies, same equipment.'),
        ('Installed, Not Subcontracted', 'Every system we sell is installed by our own team \u2014 the same people who quoted it and who handle the warranty afterward.'),
        ('Factory-Backed Equipment', 'Factory-trained installation and factory-backed equipment, with a written limited warranty on every whole-home system we put in.')
    ]

# ---------------------------------------------------------------- FAQ
FAQS = [
        ('How long does installation take?', 'Two to four hours for most systems. We schedule around you and leave the space cleaner than we found it. Same-week installation is usually available.'),
        ('How often do filters need replacement?', 'Our systems run on backwashing media beds rather than cartridges, so there is nothing to swap on a schedule. Softening resin lasts seven to twelve years and a carbon bed ten or more. Salt is the only regular consumable. We will tell you when anything is actually due.'),
        ('What does the warranty cover?', "It is tiered. Tanks and dry parts are covered for life. The control valve, circuit board and filtration media are covered for five years. Labor from the original installation is covered for one year. We are local, so you are not waiting on a national dispatch queue when something needs attention — full terms are on our warranty page."),
        ('Do you price match?', "Yes. Find the same certified system quoted for less and we'll beat it. We buy direct from the manufacturer, so there's no distributor markup baked into our price."),
        ('Do I really need a water softener in Central Florida?', "Probably. The Floridan Aquifer runs through limestone, so the water picks up calcium and magnesium on the way to your tap. Hardness varies by utility and neighborhood, and anything over 7 grains per gallon is hard enough to start costing you appliances. Whether it's right for your address is a five-minute conversation."),
        ('Can you work on a private well?', "Yes. Wells are a big part of what we do in Lake, Volusia and rural Orange County. Well water usually needs iron and sulfur treatment ahead of softening. Get a certified lab panel for bacteria and nitrate first — we'll tell you where."),
        ('How much salt will I go through?', "About one 40-pound bag a month for a family of four. If you're burning through more than that, the unit is either too small or set to regenerate too often. Both are fixable.")
    ]

# ---------------------------------------------------------------- why us
WHY = [
        ('shower', "Showers you'll actually notice", 'Soap lathers. Hair rinses clean. The film hard water leaves on your skin is gone the first time you use it.'),
        ('sparkle', 'Glassware without the spots', 'No white film, no cloudy glasses coming out of the dishwasher.'),
        ('laundry', 'Laundry that stays soft', 'Detergent finally does its job. Towels come out soft instead of stiff, and fabrics last longer.'),
        ('leaf', 'Chlorine and chloramine gone', 'Carbon filtration pulls the disinfectant taste and smell out at every tap, not just the kitchen.'),
        ('shield', 'A warranty in writing', 'Lifetime on tanks and dry parts, five years on the valve, board and media, one year of labor. The full terms are published, not buried.'),
        ('tag', 'Price-match promise', "Find the same certified system cheaper and we'll beat it. Flat installed pricing, in writing, before you commit.")
    ]

# ---------------------------------------------------------------- warranty
WARRANTY = {
    'intro': 'Every whole-home system we install carries a tiered limited warranty — lifetime on tanks and dry parts, five years on the control valve, circuit board and filtration media, and one year on labor.',
    'covered': [
        ('Storage & media tanks', 'Covered for life against defects in materials and workmanship.'),
        ('System dry parts', 'Mechanical and non-consumable components that do not come into direct contact with water — covered for life.'),
        ('Ceramic discs', 'The ceramic discs inside the rotary control valve — covered for life.'),
        ('Control valve', 'Five years against defects in materials and workmanship.'),
        ('Circuit board', 'System electronics and control board — five years.'),
        ('Filtration media', 'Softening resin, carbon and other filtration media — five years.'),
        ('Labor', 'Labor arising from the original installation — one year from the date of purchase.')
    ],
    'notes': [
        'Coverage applies to the original purchaser of a system bought from and installed by Orlando Water Pros.',
        'Coverage is valid only where the system is installed, operated and maintained according to the manufacturer\u2019s guidelines.',
        'Excluded: damage from improper installation, misuse, abuse, neglect, accidents, unauthorized modification or repair, acts of nature, and environmental factors such as flooding, freezing, or contaminant levels beyond what the system is specified to handle.',
        'Also excluded: damage from water conditions that foul filters, resin or membranes. This is exactly why we size a system to your actual water rather than guessing at it.',
        'Replacement parts are covered only for the remainder of the original warranty period. A repair does not extend or reset that period, and replacement parts must be fitted by an approved technician.',
        'Labor to replace a component under the manufacturer warranty is not included.',
        'This warranty is the exclusive remedy and is provided in place of all other warranties, express or implied, including any implied warranty of merchantability or fitness for a particular purpose. Total liability is limited to the original purchase price of the system; incidental, consequential and indirect damages are not covered.',
        'To make a claim, give us a call. You will need proof of purchase and your installation documentation; manufacturer claims also require a return authorization number, which we obtain on your behalf.'
    ]
}
