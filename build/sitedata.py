# -*- coding: utf-8 -*-
"""Shared content data for Orlando Water Pros."""

# ---------------------------------------------------------------- site config
SITE = {
        'brand': 'Orlando Water Pros',
        'region': 'Central Florida',
        'legal': 'Orlando Water Pros',
        'email': 'orlandowaterpros@gmail.com',
        'hours': 'Mon–Fri 8am–6pm · Sat 9am–2pm',
        'domain': 'orlandowaterpros.com',
        'phone_display': '(407) 555-0142',
        'phone_href': '+14075550142'
    }

# ---------------------------------------------------------------- service area
# Each city carries its real EWG Tap Water Database figures, pulled from the
# utility that actually serves it. Re-check these when EWG refreshes the data.
CITIES = [
        {
            'slug': 'orlando',
            'name': 'Orlando',
            'county': 'Orange County',
            'hard': '6–15',
            'supply': 'OUC (Floridan Aquifer wells)',
            'note': 'Orlando pulls from the Floridan Aquifer and disinfects with chloramine. Hardness swings by plant, so one neighborhood tests moderate while the next one over tests genuinely hard.',
            'issues': [
                'Chloramine taste and odor',
                'Scale on fixtures and glassware',
                'Hardness that changes block to block'
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
            'supply': 'City of St. Cloud utility',
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
            'hard': '12–18',
            'supply': 'City of Apopka utility & private wells',
            'note': 'Apopka runs harder than central Orlando. The rural areas around it are dense with private wells carrying iron and hydrogen sulfide.',
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
            'note': "Ocoee shares West Orange County's harder supply. A softener paired with a whole-home carbon filter is the usual answer here.",
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

# ---------------------------------------------------------------- products
PRODUCTS = [
        {
            'slug': 'complete-home-system',
            'name': 'Complete Home System',
            'cat': 'Whole Home',
            'tag': 'Most Popular',
            'img': 'complete-home-system.webp',
            'photo': 'Complete home system with tankless RO',
            'short': 'Whole-home softening and carbon filtration paired with the HW800 AlkaPro tankless RO. One installation covers every tap in the house.',
            'who': 'City-water homes that want one system to handle hardness, chlorine and drinking water together.',
            'bullets': [
                '48,000-grain softening capacity in a single mixed-resin tank',
                'Granular activated coconut shell carbon for chlorine and chloramine',
                'HW800 AlkaPro 7-stage tankless reverse osmosis at the kitchen sink',
                'Honest ProValve digital control with ceramic discs and 72-hour memory backup',
                '28 GPM system flow — no pressure drop across the house',
                'Upsized 64,000-grain configuration available for larger homes'
            ],
            'long': [
                'This is the system most Central Florida homes end up with. A single mixed-resin tank handles hardness and chlorine at the point of entry, so every shower, tap and appliance in the house gets treated water. Under the kitchen sink, the HW800 AlkaPro adds seven stages of reverse osmosis for drinking and cooking.',
                'The softening side runs 75 lbs of 10% crosslinked, USA-made resin with 15 lbs of coconut shell carbon and a polishing gravel bed. The resin resists chlorine and oxidation, which is what determines how long a softener actually lasts in chlorinated city water. The tank measures 12 inches across and 52 inches tall, with a 15-inch square brine tank alongside it.',
                'Control is handled by the Honest ProValve — ceramic discs instead of rubber seals, a plain-language program interface, and long-term memory that keeps your settings through a power cut. Standard capacity is 48,000 grains; if your household is large or your water tests at the high end, we size up to the 64,000-grain configuration instead.'
            ]
        },
        {
            'slug': 'city-water-dual-tank',
            'name': 'City Water Dual Tank',
            'cat': 'Whole Home',
            'img': 'city-water-dual-tank.webp',
            'photo': 'Two-tank city water system',
            'short': 'Two dedicated tanks for city water — one for filtration, one for softening. Each job gets its own media bed.',
            'who': 'City-water homes that already have drinking water covered and want the strongest whole-home treatment.',
            'bullets': [
                'Separate carbon tank removes chlorine, chloramine and sediment',
                'Separate softener tank removes calcium and magnesium hardness',
                'Each media bed sized and serviced independently',
                'WQA Gold Seal CG10 softening resin',
                'Programmable digital control valve',
                'No reverse osmosis included — pairs with either RO system'
            ],
            'long': [
                'Splitting filtration and softening across two tanks means neither job is a compromise. The first tank is a dedicated carbon bed that strips chlorine, chloramine and sediment before the water reaches anything else. The second is a full softener that handles hardness on its own.',
                'The practical advantage shows up over time. Chlorine is what degrades softening resin, so removing it upstream extends the life of the resin bed considerably. It also means each tank can be serviced on its own schedule rather than replacing a combined bed when only half of it is spent.',
                'This is the configuration we recommend when a home is on city water, already has a drinking water system, and wants whole-home treatment that will still be performing well in a decade.'
            ]
        },
        {
            'slug': 'softener-carbon-filtration',
            'name': 'Softener + Carbon Filtration',
            'cat': 'Whole Home',
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
            'slug': 'whole-home-carbon-filter',
            'name': 'Whole Home Carbon Filter',
            'cat': 'Whole Home',
            'img': 'whole-home-carbon-filter.webp',
            'photo': 'Standalone whole-home carbon filter',
            'short': 'Carbon filtration on its own, for homes that already have soft water but still taste and smell the chlorine.',
            'who': 'Homes with naturally soft water, or an existing softener, that need chlorine and chloramine gone.',
            'bullets': [
                'Granular activated coconut shell carbon',
                'Removes chlorine, chloramine, taste and odor at every tap',
                'Reduces sediment and particulates',
                'No salt, no brine tank, no regeneration',
                'Low-maintenance media with a long service life',
                'Works as a standalone unit or ahead of an existing softener'
            ],
            'long': [
                'Not every home needs softening. If your water is already soft — or you have a softener that works fine — but the shower still smells like a swimming pool, carbon filtration on its own is the right answer.',
                'The bed is granular activated coconut shell carbon, which is the same medium in our combination systems. It pulls chlorine and chloramine out of the water along with the taste and odor they carry, and it captures sediment and particulates on the way through.',
                'Installed ahead of an existing softener, it also does that softener a favor: chlorine is what breaks resin down over time, so removing it upstream buys you years of additional resin life.'
            ]
        },
        {
            'slug': 'premium-well-water-system',
            'name': 'Premium Well Water System',
            'cat': 'Well Water',
            'tag': 'Iron & Sulfur',
            'img': 'premium-well-water-system.webp',
            'photo': 'Iron and sulfur removal system with peroxide injection',
            'short': 'Iron staining and rotten-egg sulfur odor handled before the water reaches your house, with softening built in.',
            'who': 'Private wells with orange staining, sulfur smell, or both.',
            'bullets': [
                'Hydrogen peroxide injection at the point of entry',
                'Oxidizes iron, manganese and hydrogen sulfide so carbon can capture them',
                'Granular activated catalytic coconut shell carbon bed',
                '48,000-grain softening tank included',
                'Backwash self-cleaning — no cartridges to swap',
                '30 GPM valve flow, 27 GPM system flow'
            ],
            'long': [
                'Well water in Lake, Volusia and rural Orange County commonly carries dissolved iron and hydrogen sulfide. Neither can be filtered out while it is dissolved, which is why simple cartridge filters fail at this. It has to be oxidized into a solid first.',
                'This system injects hydrogen peroxide at the point of entry, where it converts dissolved iron and sulfur into particles the catalytic carbon bed can trap. The bed backwashes itself on a schedule, flushing what it caught down the drain. A holding tank keeps peroxide feeding steadily rather than in bursts.',
                'Behind the iron and sulfur stages sits a full 48,000-grain softener on a 10-inch by 54-inch media tank, so hardness is handled in the same pass. The result is water that no longer stains fixtures orange or announces itself when you turn on the tap.'
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
                'Where a well has iron and hardness but not a significant sulfur problem, a dual-tank setup is usually the better fit than a full peroxide injection system. It costs less, takes up less space, and there is no chemical to keep topped up.',
                'The first tank removes iron and sediment, protecting everything downstream from staining and abrasion. The second is a dedicated softener running WQA Gold Seal resin that handles hardness on its own bed and its own schedule.',
                'If a lab panel comes back showing hydrogen sulfide as well, we will tell you plainly that this system is not the right one and point you at the peroxide injection setup instead. Sizing a well system off a guess is how people end up replacing equipment twice.'
            ]
        },
        {
            'slug': 'salt-free-conditioner',
            'name': 'Salt-Free Conditioner',
            'cat': 'Softeners',
            'img': 'salt-free-conditioner.webp',
            'photo': 'Compact salt-free conditioner',
            'short': 'Scale protection with no salt, no drain, no power and nothing to refill. It conditions water rather than softening it.',
            'who': 'Homes where salt storage or a drain connection is a problem, or anyone avoiding a sodium byproduct.',
            'bullets': [
                'No salt to buy, haul or store',
                'No brine tank, no drain line, no electricity',
                'Keeps calcium and magnesium from bonding as scale',
                'Retains the beneficial minerals in your water',
                'Compact — a fraction of the footprint of a tank-and-brine setup',
                'Prevents scale rather than removing hardness — we will explain the difference'
            ],
            'long': [
                'A salt-free conditioner changes the form of hardness minerals so they stay suspended in the water instead of bonding to pipe walls, heating elements and fixtures. That is genuine scale protection, delivered with no salt, no drain and no power.',
                'What it will not do is remove hardness. Water leaving a conditioner still tests hard, because the calcium and magnesium are still in it. You will not get the slippery-soft shower or the improvement in soap lathering that a true ion-exchange softener gives you.',
                'For some households that trade is clearly worth it — no bags of salt to carry, no brine discharge, no drain to plumb, and the minerals stay in the water. For others it is not what they were picturing. We would rather explain the difference before we install it than after.'
            ]
        },
        {
            'slug': 'hw800-alkapro',
            'name': 'HW800 AlkaPro',
            'cat': 'Drinking Water',
            'tag': 'Flagship RO',
            'img': 'hw800-alkapro.webp',
            'photo': 'Tankless reverse osmosis unit under a kitchen sink',
            'short': 'Seven-stage tankless reverse osmosis producing 800 gallons a day, finished with alkaline remineralization. No storage tank, no wait.',
            'who': 'Anyone who wants the best drinking water we sell.',
            'bullets': [
                'Tankless — the space under your sink stays yours',
                '800 gallons per day, on demand',
                '0.0001 micron membrane rejects 95–99% of dissolved solids',
                'Targets heavy metals, microplastics, PFAS and disinfection byproducts',
                'Alkaline remineralization balances pH and restores taste',
                '2:1 low drain ratio — far less wastewater than standard RO',
                'Colour-matched faucet included, filters flagged when due'
            ],
            'long': [
                'Traditional reverse osmosis stores treated water in a pressurized bladder tank that takes up most of the cabinet, and you draw it down faster than it refills. The HW800 makes water on demand instead, at 800 gallons per day, so the space under your sink stays yours and the glass fills at full flow.',
                'Water passes through a 5-micron sediment pre-filter, then double NSF carbon blocks that absorb chloramine, THMs and TCE while preparing the water for the membrane. The membrane itself is an NSF thin film composite rated to 0.0001 microns, rejecting 95 to 99% of total dissolved solids along with heavy metals, microplastics and PFAS. Two in-line coconut shell carbon stages polish out dissolved gases and any remaining taste.',
                'The seventh stage is what most people notice. An internal alkaline remineralizer puts back the trace minerals stripped out by the membrane and balances pH, so the water tastes like water rather than like nothing. The system also runs a 2:1 drain ratio, producing two cups of purified water for every one sent to drain — a meaningful improvement on older RO designs.'
            ]
        },
        {
            'slug': '5-stage-reverse-osmosis',
            'name': '5-Stage Reverse Osmosis',
            'cat': 'Drinking Water',
            'img': '5-stage-reverse-osmosis.webp',
            'photo': 'Five-stage RO system with storage tank',
            'short': 'Proven under-sink reverse osmosis with its own faucet and storage tank. The most drinking-water quality per dollar we offer.',
            'who': 'Households that want excellent drinking water at the lowest entry price.',
            'bullets': [
                'Five stages of sediment, carbon and membrane filtration',
                'Removes up to 99% of contaminants including lead, chlorine, fluoride and nitrates',
                'Dedicated faucet at the sink, five finishes to choose from',
                'Pressurized steel storage tank with food-grade butyl bladder',
                'Simple annual filter service',
                'A design that has been around long enough to trust'
            ],
            'long': [
                'Reverse osmosis pushes water through a semi-permeable membrane that rejects dissolved solids, then polishes what comes through with carbon. Nothing else you can install in a house treats drinking water this thoroughly.',
                'This version stores its treated water in a pressurized tank, which is the trade-off against the tankless model: it needs cabinet space, and it costs less. The tank is a high-strength steel shell with a food-grade butyl bladder separating water from air, keeping the supply fresh and the pressure steady so the faucet delivers full flow every time.',
                'Filters get changed annually. The membrane runs two to three years depending on what is coming into it — harder, higher-solids water works a membrane harder. We send a reminder when yours is due.'
            ]
        },
        {
            'slug': 'pre-sediment-filter',
            'name': 'Pre-Sediment Filter',
            'cat': 'Pre-Filtration',
            'photo': '20-inch whole-house sediment pre-filter',
            'short': 'The first line of defence for everything downstream. Catches sand, silt, rust and grit before they reach your softener, RO or appliances.',
            'who': 'Homes on well water, older infrastructure, or any system worth protecting.',
            'bullets': [
                '20 inch by 4.5 inch cartridge housing',
                '15 GPM flow rate — no restriction on household pressure',
                '10,000 gallon cartridge life',
                'Removes sand, silt, rust and particulates at the main line',
                'Protects softening resin, carbon beds and RO membranes from fouling',
                'Simple cartridge change, no tools beyond a housing wrench'
            ],
            'long': [
                'Sediment gets into residential water in ordinary ways — ageing municipal mains, a water main repair down the street, natural mineral deposits, or a well drawing through sandy ground. Once it is in the line it does not stay put.',
                'Without a dedicated sediment filter, those particles accumulate inside filtration media and restrict flow. They cause premature wear on control valves, plumbing fixtures and appliances, and they foul the surface of an RO membrane, which is the most expensive component in the house to replace.',
                'Installed at the main water entry point, this filter stops debris before it reaches anything else. Reduced fouling means better flow rates, fewer service calls and more consistent pressure throughout the house. It is a small component that quietly extends the life of every system behind it.'
            ]
        }
    ]

PRODUCT_CATS = [
        'Whole Home',
        'Well Water',
        'Softeners',
        'Drinking Water',
        'Pre-Filtration'
    ]

# ------------------------------------------- manufacturer-published specs
SPECS = {
        'complete-home-system': [
            ('Softening capacity', '48,000 grains (64,000 available)'),
            ('Resin volume', '75 lbs, 10% crosslinked USA-made'),
            ('Carbon volume', '15 lbs granular activated coconut shell'),
            ('Media tank', '12" x 52"'),
            ('Brine tank', '15" x 35" square'),
            ('Valve / system flow', '28 GPM / 28 GPM'),
            ('Bypass size', '1"'),
            ('Drinking water', 'HW800 AlkaPro 7-stage tankless RO included')
        ],
        'city-water-dual-tank': [
            ('Tanks', 'Two — dedicated carbon and dedicated softener'),
            ('Media', 'CG10 softening resin, granular activated coconut shell carbon'),
            ('Resin', 'WQA Gold Seal award-winning resin'),
            ('Targets', 'Hardness, chlorine, chloramine, sediment'),
            ('Bypass size', '1"')
        ],
        'softener-carbon-filtration': [
            ('Tanks', 'Single mixed-media tank'),
            ('Media', 'High-capacity softening resin, coconut shell carbon, polishing gravel'),
            ('Targets', 'Hardness (calcium & magnesium), chlorine taste and odor'),
            ('Brine tank', '15" x 35" square')
        ],
        'whole-home-carbon-filter': [
            ('Tanks', 'Single tank'),
            ('Media', 'Granular activated coconut shell carbon, polishing gravel'),
            ('Targets', 'Chlorine, chloramine, sediment, taste and odor'),
            ('Salt / drain', 'No salt or brine tank required')
        ],
        'premium-well-water-system': [
            ('Configuration', 'Carbon filter tank, softener, peroxide injection panel and holding tank'),
            ('Softening capacity', '48,000 grains'),
            ('Resin volume', '1.5 cu ft'),
            ('Media', 'Granular activated catalytic coconut shell carbon'),
            ('Media tank', '10" x 54"'),
            ('Brine tank', '15" x 35" square'),
            ('Valve / system flow', '30 GPM / 27 GPM'),
            ('Targets', 'Iron, manganese, hydrogen sulfide, hardness')
        ],
        'well-water-dual-tank': [
            ('Tanks', 'Two — iron/sediment removal and softening'),
            ('Media', 'CG10 softening resin, granular activated coconut shell carbon, Katalox Light'),
            ('Resin', 'WQA Gold Seal award-winning resin'),
            ('Targets', 'Iron, sediment, hardness'),
            ('Bypass size', '1"')
        ],
        'salt-free-conditioner': [
            ('Tanks', 'Single tank'),
            ('Salt / brine tank', 'None required'),
            ('Drain connection', 'None required'),
            ('Power', 'None required — no valve or electronics'),
            ('Targets', 'Scale prevention (does not remove hardness)')
        ],
        'hw800-alkapro': [
            ('Type', 'Tankless reverse osmosis'),
            ('Production', '800 gallons per day'),
            ('Filtration', '7 stages'),
            ('Membrane', 'NSF thin film composite, 0.0001 micron, 95–99% rejection'),
            ('Drain ratio', '2:1 — two cups pure per one to drain'),
            ('Finish', 'Colour-matched faucet included'),
            ('Manufacturer warranty', '1-year limited')
        ],
        '5-stage-reverse-osmosis': [
            ('Type', 'Tank-style reverse osmosis'),
            ('Filtration', '5 stages'),
            ('Storage tank', 'Steel shell with food-grade butyl bladder'),
            ('Targets', 'Sediment, chlorine, lead, fluoride, nitrates, dissolved solids'),
            ('Faucet', 'Brushed nickel, chrome, brushed gold, matte black or oil-rubbed bronze'),
            ('Manufacturer warranty', '1-year limited')
        ],
        'pre-sediment-filter': [
            ('Product size', '20" x 4.5"'),
            ('Flow rate', '15 GPM'),
            ('Filter life', '10,000 gallons'),
            ('Targets', 'Sand, silt, rust, particulates'),
            ('Placement', 'Main water entry point, ahead of all other equipment')
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
        ('FL licensed plumber install', 'yes', 'Varies', 'Varies', 'Varies', 'no:DIY'),
        ('Lifetime warranty', 'yes', '1 year', '10 year', '1 year', 'no'),
        ('No long-term contracts', 'yes', 'Multi-year typical', 'Multi-year typical', 'Multi-year typical', 'N/A'),
        ('Transparent pricing', 'yes', 'no', 'no', 'no', 'yes'),
        ('Same-week installation', 'yes', '2–3 weeks', '2–3 weeks', '2–3 weeks', 'DIY timeline')
    ]

# ---------------------------------------------------------------- maintenance
MAINTENANCE = [
        ('Salt refill', '1–2 bags every 4–6 weeks', 'You buy it — about $6–8 a bag', 'Any system with a softener'),
        ('Reverse osmosis filters', 'Every 12 months', '$149', 'HW800 AlkaPro, 5-Stage RO'),
        ('Pre-sediment filter cartridge', 'Every 6 months', '$250', 'Pre-Sediment Filter'),
        ('Hydrogen peroxide', 'Every 3–8 weeks', '$75 per 5-gallon jug', 'Premium Well Water System'),
        ('Softening resin tank', 'Swap every 7–12 years', '', 'Any system with a softener'),
        ('Carbon tank', '10+ years', '', 'Dual-tank and carbon systems'),
        ('Salt-free conditioner tank', 'Swap about every 3 years', '', 'Salt-Free Conditioner')
    ]

# ---------------------------------------------------------------- credentials
CERTS = [
        ('NSF-Certified Components', 'The carbon media, gravel, holding tanks and main valves in our systems carry NSF certification, including carbon from Jacobi Carbons.'),
        ('Drinking Water System Components', 'Our components are certified under the NSF Drinking Water System Components program, the standard covering everything your water actually touches.'),
        ('Cation Exchange Water Softeners', 'Our softeners are certified under the NSF program for cation exchange water softeners, the category that covers ion-exchange performance.'),
        ('WQA Gold Seal', 'Water Quality Association Gold Seal certification, held on top of NSF certification. Two independent bodies, same equipment.'),
        ('Installed by Licensed Florida Plumbers', 'Every install is done by a licensed, insured Florida plumber.'),
        ('Factory-Backed Equipment', 'Factory-trained installation and factory-backed equipment, with a lifetime warranty on every whole-home system we put in.')
    ]

# ---------------------------------------------------------------- FAQ
FAQS = [
        ('How long does installation take?', 'Two to four hours for most systems. We schedule around you and leave the space cleaner than we found it. Same-week installation is usually available.'),
        ('How often do filters need replacement?', 'Reverse osmosis filters run twelve months and the membrane two to three years. A pre-sediment cartridge is every six months. We send a reminder when yours are due, and we will change them for you if you would rather not — give us a call and we will get you on the schedule.'),
        ('What does the lifetime warranty cover?', "On whole-home systems: tanks, valves, electronics and components, for life. Plus one year of labor. Our reverse osmosis units carry the manufacturer's 1-year limited warranty instead — see the product page for details. We're local, so you're not waiting on a national dispatch queue when something needs attention. Full terms are on our warranty page."),
        ('Do you price match?', "Yes. Find the same certified system quoted for less and we'll beat it. We buy direct from the manufacturer, so there's no distributor markup baked into our price."),
        ('Do I really need a water softener in Central Florida?', "Probably. The Floridan Aquifer runs through limestone, so most of our service area tests between 10 and 18 grains per gallon. Anything over 7 is hard enough to start costing you appliances. Whether it's right for your address is a five-minute conversation."),
        ('Can you work on a private well?', "Yes. Wells are a big part of what we do in Lake, Volusia and rural Orange County. Well water usually needs iron and sulfur treatment ahead of softening. Get a certified lab panel for bacteria and nitrate first — we'll tell you where."),
        ('How much salt will I go through?', "About one 40-pound bag a month for a family of four. If you're burning through more than that, the unit is either too small or set to regenerate too often. Both are fixable.")
    ]

# ---------------------------------------------------------------- why us
WHY = [
        ('shower', "Showers you'll actually notice", 'Soap lathers. Hair rinses clean. The film hard water leaves on your skin is gone the first time you use it.'),
        ('sparkle', 'Glassware without the spots', 'No white film, no cloudy glasses coming out of the dishwasher.'),
        ('laundry', 'Laundry that stays soft', 'Detergent finally does its job. Towels come out soft instead of stiff, and fabrics last longer.'),
        ('leaf', 'Chlorine and chloramine gone', 'Carbon filtration pulls the disinfectant taste and smell out at every tap, not just the kitchen.'),
        ('shield', 'Lifetime warranty', 'Whole-home systems carry lifetime coverage on tanks, valves, electronics and components, plus a year of labor.'),
        ('tag', 'Price-match promise', "Find the same certified system cheaper and we'll beat it. Flat installed pricing, in writing, before you commit.")
    ]

# ---------------------------------------------------------------- warranty
WARRANTY = {
        'intro': 'Every whole-home system we install carries a lifetime warranty on equipment, plus one year of labor.',
        'covered': [
            ('Tanks', 'Mineral and brine tanks, covered for life against defects in materials and workmanship.'),
            ('Valves', 'Control valves and bypass valves, covered for life.'),
            ('Electronics', 'Control heads, timers and electronic components, covered for life.'),
            ('Components', 'All remaining system components, covered for life against defects.'),
            ('Labor', 'Labor on warranty repairs, covered for one year from the installation date.')
        ],
        'notes': [
            'Coverage applies to systems bought from and installed by Orlando Water Pros.',
            "The two reverse-osmosis systems we sell — the HW800 AlkaPro and the 5-Stage Reverse Osmosis system — are covered by the manufacturer's 1-year limited warranty instead of the lifetime terms above.",
            "Coverage transfers to a new homeowner at the same service address, as long as the system hasn't been moved or modified.",
            'Coverage is voided by unauthorized modification or DIY repair, operating the system outside manufacturer specifications, damage from skipped maintenance, or freeze damage.',
            '"Lifetime" means the useful life of the original equipment at its original installation address — it doesn\'t transfer with the equipment if it\'s relocated to a different property.',
            "Consumables are maintenance items and aren't covered. That means filter cartridges and media — see the service intervals below.",
            'To make a claim, give us a call. We handle warranty service ourselves.'
        ]
    }

