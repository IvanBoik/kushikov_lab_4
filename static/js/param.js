// Параметры
        const params = {
            0: [true, true, true, true, true],

            1: [false, true, true, true, true],
            2: [true, false, true, true, true],
            3: [true, true, false, true, true],
            4: [true, true, true, false, true],
            5: [true, true, true, true, false],

            6: [false, false, true, true, true],
            7: [false, true, false, true, true],
            8: [true, true, false, false, true],
            9: [false, true, true, false, true],
            10: [false, true, true, true, false],
            11: [true, false, true, false, true],
            12: [true, false, true, true, false],
            13: [true, true, false, false, true],
            14: [true, true, false, true, false],
            15: [true, true, true, false, false],

            16: [false, false, false, true, true],
            17: [false, false, true, false, true],
            18: [false, false, true, true, false],
            19: [false, true, false, false, true],
            20: [false, true, false, true, false],
            21: [true, false, false, false, true],
            22: [true, false, false, true, false],
            23: [false, true, true, false, false],
            24: [true, false, true, false, false],
            25: [true, true, false, false, false],

            26: [false, false, false, false, true],
            27: [false, false, false, true, false],
            28: [false, false, true, false, false],
            29: [false, true, false, false, false],
            30: [true, false, false, false, false],

            31: [],
        }

        const paramsDiv = document.querySelector("#main .values .p0 .inputs")

        for(let key in params){
            paramsDiv.innerHTML +=
            `<div class="input-block">
                <label for="P${key}" style="display: flex; justify-content: space-between;"><span>P<sub>${key}</sub> - Вероятность того, что
                ${params[key].length == 0 ? 'ПК1-ПК5 не работают' : 'работают ПК:'}
                ${params[key][0] ? '1, ' : ''}
                ${params[key][1] ? '2, ' : ''}
                ${params[key][2] ? '3, ' : ''}
                ${params[key][3] ? '4, ' : ''}
                ${params[key][4] ? '5, ' : ''}</span>
                <span>Нач. знач. = </span></label>
                <input id="P${key}" type="number" step="0.001" min="0" max="1" required value="0">
            </div>`;
        }
        paramsDiv.querySelector("#P0").value = 1;

        // Константы
        const ls = {
            "l1": "Интенсивность отказа ПК1",
            "l2": "Интенсивность отказа ПК2",
            "l3": "Интенсивность отказа ПК3",
            "l4": "Интенсивность отказа ПК4",
            "l5": "Интенсивность отказа ПК5",
        }

        const lsDiv = document.querySelector("#main .values .l .inputs")

        for(let key in ls){
            main_key = key.replace(/[0-9]/, '');
            sub_key = key.replace(main_key, '');
            lsDiv.innerHTML +=
            `<div class="input-block">
                <label for="${key}">λ${sub_key ? `<sub>${sub_key}</sub>` : ''} - ${ls[key]}</label>
                <input id="${key}" type="number" step="0.001" min="0" required value="1">
            </div>`;
        }

        // Константы
        const us = {
            "u1": "Интенсивность восстановления ПК1",
            "u2": "Интенсивность восстановления ПК2",
            "u3": "Интенсивность восстановления ПК3",
            "u4": "Интенсивность восстановления ПК4",
            "u5": "Интенсивность восстановления ПК5",
        }

        const usDiv = document.querySelector("#main .values .u .inputs")

        for(let key in us){
            main_key = key.replace(/[0-9]/, '');
            sub_key = key.replace(main_key, '');
            usDiv.innerHTML +=
            `<div class="input-block">
                <label for="${key}">μ${sub_key ? `<sub>${sub_key}</sub>` : ''} - ${us[key]}</label>
                <input id="${key}" type="number" step="0.001" min="0" required value="2.5">
            </div>`;
        }