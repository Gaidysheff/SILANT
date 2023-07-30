
menu = [
    {'title': "Главная страница", 'url_name': 'index'},
    {'title': "Моя база данных", 'url_name': 'page_after_authorization'},
    {'title': "СПРАВОЧНИКИ", 'url_name': 'all_directories'},
    {'title': "Добавить машину", 'url_name': 'add_machine'},
    {'title': "Добавить ТО", 'url_name': 'add_maintenance'},
    {'title': "Добавить рекламацию", 'url_name': 'add_claim'},
    {'title': "О сайте", 'url_name': 'about'},
]


machine_table_titles = ['Машина', 'Двигатель', 'Трансмиссия', 'Ведущий мост',
                        'Управляемый мост', 'Договор и Отгрузка', 'Грузополучатель', 'Дополнительно']

directories = ['Наименование', 'Описание']


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        context['machine_table_titles'] = machine_table_titles
        context['directories'] = directories
        return context
