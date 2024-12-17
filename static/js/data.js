 const getData = () => {
            const form = document.querySelector("#main");

            //шаблон JSON-оъекта
            let data = {
                'p0': {},
                'c': {},
                't': 1,
                'p': 1,
            };

            //из каждого '.p0 .input-block' элемента, состоящего из input с данными о начальных значениях извлекаем значения
            let p0s = form.querySelectorAll(".p0 .input-block");
            for (let i = 0; i < p0s.length; i++) {
                let key = `P${i}`;
                data['p0'][key] = Number(p0s[i].querySelector(`#${key}`).value);
            }

            //из каждого '.l .input-block' элемента, состоящего из input с данными о значениях отказа извлекаем значения
            let ls = form.querySelectorAll(".l .input-block");
            for (let i = 0; i < ls.length; i++) {
                let key = `l${i+1}`;
                data['c'][key] = Number(ls[i].querySelector(`#${key}`).value);
            }

            //из каждого '.u .input-block' элемента, состоящего из input с данными о значениях восстановления извлекаем значения
            let us = form.querySelectorAll(".u .input-block");
            for (let i = 0; i < ls.length; i++) {
                let key = `u${i+1}`;
                data['c'][key] = Number(us[i].querySelector(`#${key}`).value);
            }

            //извлекаем интервал и шаг
            data['t'] = 1;
            data['m'] = 1;

            return data;
        }