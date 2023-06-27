
menu = [
    {'title': "Главная страница", 'url_name': 'index'},
    {'title': "Добавить статью", 'url_name': 'add_page'},
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Обратная связь", 'url_name': 'contact'},
    # {'title': "Войти", 'url_name': 'login'},
]


machine_table_titles = ['Машина', 'Двигатель', 'Трансмиссия', 'Ведущий мост',
                        'Управляемый мост', 'Договор и Отгрузка', 'Грузополучатель', 'Дополнительно']

# machine_table_subtitles = ['Модель техники', 'Зав. № машины', 'Модель двигател', 'Зав. № двигателя', 'Модель трансмиссии', 'Зав. № трансмиссии', 'Модель ведущего моста', 'Зав. № ведущего моста', 'Модель управляемого моста',
#                            'Зав. № управляемого моста', 'Договор поставки №, дата', 'Грузополучатель (конечный потребитель)', 'Адрес поставки (эксплуатации)', 'Комплектация (дополнительные опции)', 'Клиент', 'Сервисная компания']

directories = ['Наименование', 'Описание']


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        context['machine_table_titles'] = machine_table_titles
        context['directories'] = directories
        return context