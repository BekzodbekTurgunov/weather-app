from loader import dp
from .is_admin import AdminFilter
from .is_group import IsGroup
from .is_private import IsPrivate


if __name__ == "filters":
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(AdminFilter)
    # pass
