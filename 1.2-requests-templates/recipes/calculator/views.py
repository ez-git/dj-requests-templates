from django.shortcuts import render


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'butter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def get_recipe(request, recipe_name):

    context = {
        'recipe': DATA.get(recipe_name, {}).copy()
    }

    if not context['recipe'] is None:
        serving = int(request.GET.get('serving', 1))
        if serving > 1:
            for key, value in context['recipe'].items():
                context['recipe'][key] = round(value * serving,
                                               len(str(value).split('.')[-1]))

    return render(request, 'calculator/index.html', context)
