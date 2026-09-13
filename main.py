import logging
import os

import telebot
from telebot import types


BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()
if not BOT_TOKEN:
    raise RuntimeError(
        "TELEGRAM_BOT_TOKEN is not set. Add it to the project's secure secrets."
    )

WEB_APP_URL = os.environ.get("WEB_APP_URL", "https://www.lesoir.be").strip()

bot = telebot.TeleBot(BOT_TOKEN)

bot.set_chat_menu_button(
    menu_button=types.MenuButtonWebApp(
        type="web_app",
        text="Ouvrir Le Soir",
        web_app=types.WebAppInfo(url=WEB_APP_URL),
    )
)

# ============================================
# SCREEN 1 — START
# ============================================
@bot.message_handler(commands=["start"])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn_open = types.InlineKeyboardButton(
        text="📰 Ouvrir Le Soir",
        web_app=types.WebAppInfo(url=WEB_APP_URL),
    )
    btn_headlines = types.InlineKeyboardButton(
        text="📋 Les titres du jour", callback_data="headlines"
    )
    btn_summary = types.InlineKeyboardButton(
        text="🏛 Sommaire", callback_data="sommaire"
    )
    markup.add(btn_open)
    markup.row(btn_headlines, btn_summary)

    text = (
        "📰 *Bienvenue sur Le Soir.*\n\n"
        "_«Un journal est un dialogue quotidien avec ses lecteurs.»_\n\n"
        "Depuis *1887*, ce dialogue se poursuit — sur papier, sur le web, "
        "et aujourd'hui ici sur Telegram. Chaque saison une petite "
        "sélection de culture, voyages, cuisine, science et sport, "
        "à lire tranquillement en chat.\n\n"
        "Pour commencer, appuyez sur *Les titres du jour*."
    )

    bot.send_message(
        message.chat.id,
        text,
        parse_mode="Markdown",
        reply_markup=markup,
    )


# ============================================
# SCREEN 2 — HEADLINES
# ============================================
@bot.callback_query_handler(func=lambda call: call.data == "headlines")
def headlines(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton(
            text="🎨 Culture — expositions d'automne",
            callback_data="culture",
        ),
        types.InlineKeyboardButton(
            text="🍺 Cuisine — spécialités belges",
            callback_data="cuisine",
        ),
        types.InlineKeyboardButton(
            text="🏠 Voyages — cinq villages cachés",
            callback_data="travel",
        ),
        types.InlineKeyboardButton(
            text="🏛 Sommaire",
            callback_data="sommaire",
        ),
    )

    text = (
        "📋 *Les titres du jour*\n\n"
        "Trois lectures choisies pour aujourd'hui. Chacune lisible "
        "en entier dans le chat.\n\n"
        "*Culture* — expositions d'automne : cinq rendez-vous "
        "à ne pas manquer dans les musées belges.\n\n"
        "*Cuisine* — spécialités belges : quatre recettes classiques "
        "de la tradition régionale.\n\n"
        "*Voyages* — cinq villages belges à découvrir "
        "le temps d'un week-end d'automne.\n\n"
        "Appuyez sur un titre pour ouvrir l'article complet."
    )

    bot.send_message(
        call.message.chat.id,
        text,
        parse_mode="Markdown",
        reply_markup=markup,
    )


# ============================================
# SCREEN 3 — CULTURE
# ============================================
@bot.callback_query_handler(func=lambda call: call.data == "culture")
def culture(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton(
            text="📰 Ouvrir Le Soir",
            web_app=types.WebAppInfo(url=WEB_APP_URL),
        )
    )
    markup.row(
        types.InlineKeyboardButton(
            text="📋 Les titres du jour",
            callback_data="headlines",
        ),
        types.InlineKeyboardButton(
            text="🏛 Sommaire",
            callback_data="sommaire",
        ),
    )

    text = (
        "🎨 *Expositions d'automne : cinq rendez-vous dans les musées belges*\n\n"
        "Les musées rouvrent avec la nouvelle saison. Cinq rendez-vous "
        "qui méritent votre attention cet automne.\n\n"
        "*Bruxelles — Magritte et le surréalisme*\n"
        "Le Musée Magritte présente une rétrospective inédite avec "
        "des œuvres rarement exposées, prêtées par des collections "
        "privées du monde entier. Un dialogue entre rêve et réalité.\n\n"
        "*Anvers — Rubens redécouvert*\n"
        "Le Musée Royal des Beaux-Arts propose une relecture de "
        "l'œuvre de Rubens à travers les techniques de restauration "
        "modernes. Des détails invisibles depuis quatre siècles.\n\n"
        "*Gand — art contemporain flamand*\n"
        "Le S.M.A.K. accueille une nouvelle génération d'artistes "
        "belges. Installations, vidéo et sculpture dans un dialogue "
        "avec la collection permanente.\n\n"
        "*Liège — photographie industrielle*\n"
        "La Boverie expose un siècle d'images du bassin sidérurgique "
        "wallon. Regard documentaire et poétique sur un monde disparu.\n\n"
        "*Bruges — manuscrits médiévaux*\n"
        "Le Groeningemuseum dévoile des manuscrits enluminés du "
        "XVe siècle. Une occasion rare de voir des trésors "
        "habituellement conservés en réserve.\n\n"
        "_Dates et horaires à vérifier sur les sites officiels des musées._"
    )

    bot.send_message(
        call.message.chat.id,
        text,
        parse_mode="Markdown",
        reply_markup=markup,
    )


# ============================================
# SCREEN 4 — CUISINE
# ============================================
@bot.callback_query_handler(func=lambda call: call.data == "cuisine")
def cuisine(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton(
            text="📰 Ouvrir Le Soir",
            web_app=types.WebAppInfo(url=WEB_APP_URL),
        )
    )
    markup.row(
        types.InlineKeyboardButton(
            text="📋 Les titres du jour",
            callback_data="headlines",
        ),
        types.InlineKeyboardButton(
            text="🏛 Sommaire",
            callback_data="sommaire",
        ),
    )

    text = (
        "🍺 *Spécialités belges : quatre recettes classiques*\n\n"
        "La cuisine belge est l'une des plus riches d'Europe. "
        "Quatre recettes pour en apprécier les saveurs.\n\n"
        "*Carbonade flamande*\n"
        "Bœuf mijoté dans une bière brune avec du pain d'épices "
        "et de la moutarde. Cuisson lente pendant deux heures. "
        "Servir avec des frites, évidemment.\n\n"
        "*Moules-frites*\n"
        "Moules fraîches cuites au vin blanc avec céleri, oignon "
        "et persil. Les frites belges sont coupées épaisses et frites "
        "deux fois dans du blanc de bœuf. Le plat national.\n\n"
        "*Waterzooi gantois*\n"
        "Ragoût crémeux de poulet ou de poisson avec carottes, "
        "poireaux et pommes de terre. Originaire de Gand, c'est "
        "le plat réconfortant par excellence des jours d'automne.\n\n"
        "*Gaufres de Liège*\n"
        "Pâte briochée avec perles de sucre. Cuisson au gaufrier "
        "jusqu'à caramélisation. Chaudes, elles sont irrésistibles. "
        "Le secret : la qualité du beurre.\n\n"
        "_Les doses et les temps s'adaptent au goût personnel._"
    )

    bot.send_message(
        call.message.chat.id,
        text,
        parse_mode="Markdown",
        reply_markup=markup,
    )


# ============================================
# SCREEN 5 — TRAVEL
# ============================================
@bot.callback_query_handler(func=lambda call: call.data == "travel")
def travel(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton(
            text="📰 Ouvrir Le Soir",
            web_app=types.WebAppInfo(url=WEB_APP_URL),
        )
    )
    markup.row(
        types.InlineKeyboardButton(
            text="📋 Les titres du jour",
            callback_data="headlines",
        ),
        types.InlineKeyboardButton(
            text="🏛 Sommaire",
            callback_data="sommaire",
        ),
    )

    text = (
        "🏠 *Cinq villages belges pour l'automne*\n\n"
        "Loin des destinations les plus fréquentées, cinq petits "
        "villages qui montrent leur plus beau côté en automne.\n\n"
        "*Durbuy (Luxembourg)*\n"
        "La plus petite ville du monde, dit-on. Ruelles médiévales, "
        "restaurants gastronomiques et le parc des Topiaires. "
        "Parfait pour un week-end romantique.\n\n"
        "*Crupet (Namur)*\n"
        "Un village de carte postale avec son donjon du XIIe siècle "
        "et sa grotte dédiée à Saint-Antoine. Les couleurs d'automne "
        "y sont spectaculaires.\n\n"
        "*Torgny (Luxembourg)*\n"
        "Le village le plus méridional de Belgique. Toits en tuiles "
        "romaines, vignobles et un microclimat étonnamment doux. "
        "On se croirait en Provence.\n\n"
        "*Redu (Luxembourg)*\n"
        "Le village du livre. Vingt-cinq bouquinistes dans un "
        "village de quatre cents habitants. Flânerie littéraire "
        "et promenades en forêt d'Ardenne.\n\n"
        "*Foy-Notre-Dame (Namur)*\n"
        "Un hameau autour d'une église du XVIIe siècle avec un "
        "plafond peint remarquable. Sentiers de randonnée à travers "
        "les collines boisées de la Meuse.\n\n"
        "_Pour l'hébergement, réservation en semaine recommandée._"
    )

    bot.send_message(
        call.message.chat.id,
        text,
        parse_mode="Markdown",
        reply_markup=markup,
    )


# ============================================
# SCREEN 6 — SOMMAIRE
# ============================================
@bot.callback_query_handler(func=lambda call: call.data == "sommaire")
def sommaire(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton(
            text="📰 Ouvrir Le Soir",
            web_app=types.WebAppInfo(url=WEB_APP_URL),
        )
    )
    markup.add(
        types.InlineKeyboardButton(
            text="📋 Les titres du jour",
            callback_data="headlines",
        )
    )
    markup.row(
        types.InlineKeyboardButton(
            text="📖 Glossaire",
            callback_data="glossaire",
        ),
        types.InlineKeyboardButton(
            text="❓ Questions fréquentes",
            callback_data="faq",
        ),
    )
    markup.row(
        types.InlineKeyboardButton(
            text="✏️ Contact rédaction",
            callback_data="contact",
        ),
        types.InlineKeyboardButton(
            text="🏛 Sur Le Soir",
            callback_data="about",
        ),
    )

    text = (
        "🏛 *Sommaire*\n\n"
        "Depuis ce menu vous pouvez :\n\n"
        "• Lire *les titres du jour* et nos articles, directement ici.\n"
        "• Consulter les rubriques : Culture, Voyages, Cuisine, "
        "Science, Sport, Économie pratique.\n"
        "• Parcourir le glossaire et les questions fréquentes.\n"
        "• Connaître l'histoire du journal et contacter la rédaction.\n\n"
        "Pour l'édition intégrale, utilisez le bouton d'ouverture ci-dessous."
    )

    bot.send_message(
        call.message.chat.id,
        text,
        parse_mode="Markdown",
        reply_markup=markup,
    )


# ============================================
# SCREEN 7 — GLOSSAIRE
# ============================================
@bot.callback_query_handler(func=lambda call: call.data == "glossaire")
def glossaire(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton(
            text="📋 Les titres du jour",
            callback_data="headlines",
        )
    )
    markup.add(
        types.InlineKeyboardButton(
            text="🏛 Sommaire",
            callback_data="sommaire",
        )
    )

    text = (
        "📖 *Petit glossaire*\n\n"
        "Quelques termes récurrents dans ces rubriques :\n\n"
        "*Rédaction* — équipe qui rassemble, sélectionne et prépare "
        "les textes pour la publication.\n\n"
        "*Éditorial* — article de réflexion, souvent signé, qui ouvre "
        "une section ou une page.\n\n"
        "*Photoreportage* — récit journalistique construit autour "
        "d'une série de photographies.\n\n"
        "*Contenu evergreen* — texte dont l'actualité ne dépend pas "
        "d'une nouvelle du jour : culture, voyages, cuisine.\n\n"
        "*Envoyé spécial* — journaliste qui couvre les nouvelles "
        "sur le terrain.\n\n"
        "*Rubrique* — section récurrente du journal consacrée à un "
        "thème spécifique.\n\n"
        "_Termes utilisés selon l'usage courant du journalisme belge._"
    )

    bot.send_message(
        call.message.chat.id,
        text,
        parse_mode="Markdown",
        reply_markup=markup,
    )


# ============================================
# SCREEN 8 — FAQ
# ============================================
@bot.callback_query_handler(func=lambda call: call.data == "faq")
def faq(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton(
            text="📋 Les titres du jour",
            callback_data="headlines",
        )
    )
    markup.add(
        types.InlineKeyboardButton(
            text="🏛 Sommaire",
            callback_data="sommaire",
        )
    )

    text = (
        "❓ *Questions fréquentes*\n\n"
        "*Ce bot est-il officiel ?*\n"
        "Cette version Telegram permet de lire en chat les contenus "
        "evergreen du Soir. L'activité éditoriale est assurée par "
        "la rédaction ; les contacts sont dans la section Contact.\n\n"
        "*À quelle fréquence est-il mis à jour ?*\n"
        "La sélection en chat est renouvelée chaque saison. Pour "
        "l'édition actualisée, utilisez le bouton d'ouverture.\n\n"
        "*Comment couper les notifications ?*\n"
        "Depuis les paramètres du chat Telegram, vous pouvez "
        "mettre en sourdine ou désactiver complètement les notifications.\n\n"
        "*Puis-je partager un article ?*\n"
        "Oui. Utilisez les options de partage intégrées de Telegram "
        "pour transférer le message dans un autre chat ou une application."
    )

    bot.send_message(
        call.message.chat.id,
        text,
        parse_mode="Markdown",
        reply_markup=markup,
    )


# ============================================
# SCREEN 9 — CONTACT
# ============================================
@bot.callback_query_handler(func=lambda call: call.data == "contact")
def contact(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.row(
        types.InlineKeyboardButton(
            text="🏛 Sommaire",
            callback_data="sommaire",
        ),
        types.InlineKeyboardButton(
            text="🏛 Sur Le Soir",
            callback_data="about",
        ),
    )

    text = (
        "✏️ *Contact rédaction*\n\n"
        "Pour la correspondance éditoriale :\n"
        "• E-mail : courrier@lesoir.be\n"
        "• Service lecteurs : lesoir.be/contact\n\n"
        "*Éditeur*\n"
        "Rossel & Cie S.A.\n"
        "Rue Royale 100\n"
        "1000 Bruxelles\n"
        "Belgique\n\n"
        "Signalements, droits de réponse et observations des lecteurs "
        "sont gérés par le service lecteurs les jours ouvrables."
    )

    bot.send_message(
        call.message.chat.id,
        text,
        parse_mode="Markdown",
        reply_markup=markup,
    )


# ============================================
# SCREEN 10 — ABOUT
# ============================================
@bot.callback_query_handler(func=lambda call: call.data == "about")
def about(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton(
            text="📰 Ouvrir Le Soir",
            web_app=types.WebAppInfo(url=WEB_APP_URL),
        )
    )
    markup.row(
        types.InlineKeyboardButton(
            text="🏛 Sommaire",
            callback_data="sommaire",
        ),
        types.InlineKeyboardButton(
            text="✏️ Contact",
            callback_data="contact",
        ),
    )

    text = (
        "🏛 *Sur Le Soir*\n\n"
        "_Le Soir_ a été fondé à Bruxelles en *1887* par Emile Rossel. "
        "Depuis sa création, le journal s'est imposé comme l'un des "
        "quotidiens francophones les plus lus de Belgique.\n\n"
        "Aujourd'hui Le Soir fait partie du *Groupe Rossel*, "
        "l'un des principaux groupes de presse en Belgique francophone. "
        "Il poursuit la production de contenus en culture, voyages, "
        "cuisine, science, sport et économie pratique.\n\n"
        "Entre édition papier, site et application mobile, Le Soir "
        "atteint quotidiennement des centaines de milliers de lecteurs. "
        "Le siège est à Bruxelles ; le site est lesoir.be.\n\n"
        "Cette version Telegram est pensée pour rendre plus confortable "
        "la lecture des contenus evergreen depuis l'interface de chat."
    )

    bot.send_message(
        call.message.chat.id,
        text,
        parse_mode="Markdown",
        reply_markup=markup,
    )


def main() -> None:
    logging.basicConfig(
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        level=logging.INFO,
    )
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.getLogger("requests").setLevel(logging.WARNING)
    logging.info("Le Soir bot is starting")
    bot.infinity_polling(skip_pending=True)


if __name__ == "__main__":
    main()
