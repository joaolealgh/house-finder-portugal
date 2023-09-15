
def load_config(website):
    config = {}
    if website == 'supercasa':
        ignored_paths = [
            'https://supercasa.pt/en-gb/',
            'https://supercasa.pt/fr-fr/',
            'https://supercasa.pt/es-es/',
            'https://supercasa.pt/de-de/',
            'https://supercasa.pt/nl-nl/',
            'https://supercasa.pt/ru-ru/',
            'https://supercasa.pt/zh-cn/',
            'https://supercasa.pt/inserir-anuncio',
            'https://supercasa.pt/inserir-anuncio',
            'https://supercasa.pt/credito-habitacao',
            'https://supercasa.pt/noticias',
            'https://www.janeladigital.com/?utm_source=supercasa/#recruitContent',
            'https://www.facebook.com/supercasa.pt',
            'https://www.instagram.com/supercasa.pt/',
            'https://www.youtube.com/channel/UCR5B6peGL3dnkZzgtsv2oWg',
            'https://www.linkedin.com/company/79883090',
            'https://twitter.com/supercasapt',
            'https://www.tiktok.com/@supercasa.pt?',
            'https://supercasa.pt/login',
            'https://infocasa.pt/',
            'https://apps.apple.com/pt/app/id1575765638#?platform=iphone',
            'https://play.google.com/store/apps/details?id=com.janeladigital.supercasamobile',
            'https://www.egorealestate.com/',
            'https://supercasa.pt/contactos',
            'https://www.livroreclamacoes.pt/inicio',
            'https://supercasa.pt/en-gb/noticias',
            'https://play.google.com',
            'https://apps.apple.com/pt/app/id1575765638#?platform=iphone',
            'https://play.google.com/store/apps/details?id=com.janeladigital.supercasamobile',
            'https://supercasa.pt/Images',
            'https://www.linkedin.com',
        ]

        house_location_list = [
            'https://supercasa.pt/comprar-casas/coimbra-distrito',
            'https://supercasa.pt/comprar-casas/algarve-distrito',
            'https://supercasa.pt/comprar-casas/lisboa-distrito',
            'https://supercasa.pt/comprar-casas/porto-distrito',
            'https://supercasa.pt/comprar-casas/santarem-distrito',
            'https://supercasa.pt/comprar-casas/leiria-distrito',
            'https://supercasa.pt/comprar-casas/setubal-distrito'
        ]

        config['ignored_paths'] = ignored_paths
        config['house_location_list'] = house_location_list
    return config