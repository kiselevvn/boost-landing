DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# CONSTANCE_BACKEND = "constance.backends.database.DatabaseBackend"
# CONSTANCE_ADDITIONAL_FIELDS = {
#     "image_field": ["django.forms.ImageField", {"required": False}]
# }
# CONSTANCE_CONFIG = {
#     "DOMAIN": (
#         "test.test",
#         "Домен сайта",
#         str,
#     ),
#     "LOGO_TEXT": (
#         "Antique-Store",
#         "Текстовый логотип сайта",
#         str,
#     ),
#     "SITE_NAME": (
#         "Магазин антиквариата",
#         "Наименованиее сайта",
#         str,
#     ),
#     "SITE_TITLE": (
#         "Интернет Магазин Антиквариата",
#         "Заголовок",
#         str,
#     ),
#     "SITE_OFFER": (
#         "Получи скидку до 40%",
#         "Предложение",
#         str,
#     ),
#     "SITE_DESCRIPTION": (
#         "У нас Вы найдёте всё, что Вам так нужно. Ассортимент магазина постоянно расширяется и дополняется в зависимости от пожеланий клиентов.",
#         "Описание сайта",
#         str,
#     ),
#     "CONTACT_PHONE": (
#         "+0 (000) 000-00-00",
#         "Контактный телефон",
#         str,
#     ),
#     "CONTACT_EMAIL": (
#         "example@example.com",
#         "Электронная Почта",
#         str,
#     ),
#     "CONTACT_TIME": (
#         "Пн - Пт, c 8:00 до 10:00",
#         "Наименованиее сайта",
#         str,
#     ),
# }

# CONSTANCE_CONFIG_FIELDSETS = {
#     "Логотип": ("LOGO_TEXT",),
#     "Главнная секция сайта": (
#         "SITE_NAME",
#         "SITE_TITLE",
#         "SITE_OFFER",
#         "SITE_DESCRIPTION",
#     ),
#     "Контакты": (
#         "CONTACT_PHONE",
#         "CONTACT_EMAIL",
#         "CONTACT_TIME",
#         "DOMAIN",
#     ),
# }

# CKEDITOR_UPLOAD_PATH = "uploads/"

# CKEDITOR_CONFIGS = {
#     "default": {
#         "skin": "moono",
#         "toolbar_Basic": [["Source", "-", "Bold", "Italic"]],
#         "toolbar_YourCustomToolbarConfig": [
#             {
#                 "name": "document",
#                 "items": [
#                     "Source",
#                     "-",
#                     "Save",
#                     "NewPage",
#                     "Preview",
#                     "Print",
#                     "-",
#                     "Templates",
#                 ],
#             },
#             {
#                 "name": "clipboard",
#                 "items": [
#                     "Cut",
#                     "Copy",
#                     "Paste",
#                     "PasteText",
#                     "PasteFromWord",
#                     "-",
#                     "Undo",
#                     "Redo",
#                 ],
#             },
#             {
#                 "name": "editing",
#                 "items": ["Find", "Replace", "-", "SelectAll"],
#             },
#             {
#                 "name": "forms",
#                 "items": [
#                     "Form",
#                     "Checkbox",
#                     "Radio",
#                     "TextField",
#                     "Textarea",
#                     "Select",
#                     "Button",
#                     "ImageButton",
#                     "HiddenField",
#                 ],
#             },
#             "/",
#             {
#                 "name": "basicstyles",
#                 "items": [
#                     "Bold",
#                     "Italic",
#                     "Underline",
#                     "Strike",
#                     "Subscript",
#                     "Superscript",
#                     "-",
#                     "RemoveFormat",
#                 ],
#             },
#             {
#                 "name": "paragraph",
#                 "items": [
#                     "NumberedList",
#                     "BulletedList",
#                     "-",
#                     "Outdent",
#                     "Indent",
#                     "-",
#                     "Blockquote",
#                     "CreateDiv",
#                     "-",
#                     "JustifyLeft",
#                     "JustifyCenter",
#                     "JustifyRight",
#                     "JustifyBlock",
#                     "-",
#                     "BidiLtr",
#                     "BidiRtl",
#                     "Language",
#                 ],
#             },
#             {"name": "links", "items": ["Link", "Unlink", "Anchor"]},
#             {
#                 "name": "insert",
#                 "items": [
#                     "Image",
#                     "Flash",
#                     "Table",
#                     "HorizontalRule",
#                     "Smiley",
#                     "SpecialChar",
#                     "PageBreak",
#                     "Iframe",
#                 ],
#             },
#             "/",
#             {
#                 "name": "styles",
#                 "items": ["Styles", "Format", "Font", "FontSize"],
#             },
#             {"name": "colors", "items": ["TextColor", "BGColor"]},
#             {"name": "tools", "items": ["Maximize", "ShowBlocks"]},
#             {"name": "about", "items": ["About"]},
#             "/",  # put this to force next toolbar on new line
#             {
#                 "name": "yourcustomtools",
#                 "items": [
#                     # put the name of your editor.ui.addButton here
#                     "Preview",
#                     "Maximize",
#                 ],
#             },
#         ],
#         "toolbar": "YourCustomToolbarConfig",
#         "tabSpaces": 4,
#         "extraPlugins": ",".join(
#             [
#                 "uploadimage",
#                 "div",
#                 "autolink",
#                 "autoembed",
#                 "embedsemantic",
#                 "autogrow",
#                 "widget",
#                 "lineutils",
#                 "clipboard",
#                 "dialog",
#                 "dialogui",
#                 "elementspath",
#             ]
#         ),
#     }
# }
