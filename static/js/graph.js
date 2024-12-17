//Инициализация холстов для отрисовки графика и лепестковых диаграмм с применением Chart.js
        const plot = document.getElementById('plot');
        const plot2 = document.getElementById('plot2');
        let chart;
        let chart2;

        //основные элементы страницы
        const form = document.querySelector("#main");

        //при отправке формы - формируем JSON-объект, требуемый для POST-запроса на вычиления
        form.onsubmit = (e) => {
            e.preventDefault();

            let localData = getData();

            //выполняем запрос при помощи FETCH
            fetch('/api/count', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json;charset=utf-8'
                },
                body: JSON.stringify(localData)
            })
                .then(res => res.json())
                .then(res => {
                    // на основе полученного ответа отриосвываем графики, на ранее заданных холстах:
                    console.log(res)
                    let sol = res['solution'];
                    let t = res['time'];
                    creatrGraph(sol, t, localData.m);
                })
                .catch(e => alert("Решение не найдено!"));
                ;
        }

        //отрисовка графиков изменения параметров xi(t) на основе объекта решений solution
        const creatrGraph = (solution, time, maxY) => {

            //удаляем старый график
            chart?.destroy();
            chart2?.destroy();

            //готовим шаблон для построения графика
            let data = {
                labels: time,
                datasets: [],
            }

            let data2 = {
                labels: time.filter((v,i) => i<time.length/2.5),
                datasets: [],
            }


            for (let i = 0; i < solution[0].length; i++) {

                let values = [];
                for (let j = 0; j < solution.length; j++) {
                    values.push(solution[j][i]);
                }

                let dataset = {
                    label: 'P'+i,
                    data: values,
                    fill: false,
                    borderColor: getColor(i),
                    tension: 0.1,
                    pointRadius: 3,
                    borderDash: getLineStyle(i),
                }
                data.datasets.push(dataset);


                let dataset2 = {
                    label: 'P'+i,
                    data: values.filter((v,i) => i<values.length/2.5).map(i => i > 0.4 ? null : i),
                    fill: false,
                    borderColor: getColor(i),
                    tension: 0.1,
                    pointRadius: 3,
                    borderDash: getLineStyle(i),
                }
                data2.datasets.push(dataset2);
            }

            // Отрисовываем график
            chart = new Chart(plot, {
                type: 'line',
                data: data,
                options: {
                    plugins: {
                        legend: {
                            display: true,
                            position: 'right',
                            align: 'center',
                            fullSize:true,
                            labels: {
                                boxWidth: 20
                            }
                         }
                    },
                }
            });

            // Отрисовываем график
            chart2 = new Chart(plot2, {
                type: 'line',
                data: data2,
                options: {
                    plugins: {
                        legend: {
                            display: true,
                            position: 'right',
                            align: 'center',
                            fullSize:true,
                            labels: {
                                boxWidth: 20
                            }
                         }
                    },
                }
            });
        }

        const colors = ["#4800FF","#0094FF","#00FFFF","#89BF00","#00FF21","#FF9400","#007F46","#C600AC","#BC0051","#57007F","#B200FF"];

        function getColor(i) {
            return colors[i%colors.length];
        }

        function getLineStyle(i) {
            if (i <= colors.length - 1) return [];
            if (i <= 2*colors.length - 1) return [5, 2];
            if (i <= 3*colors.length - 1) return [20, 5, 20, 5];
        }

        function fillInputsWithRandomValues() {
            const inputs = document.querySelectorAll("input[type='number']"); // Находим все числовые инпуты
            inputs.forEach(input => {
                const min = parseFloat(input.min) || 0; // Минимальное значение
                const max = parseFloat(input.max) || 1; // Максимальное значение
                const step = parseFloat(input.step) || 0.001; // Шаг изменения

                // Генерация случайного значения с учетом шага
                const randomValue = Math.floor((Math.random() * (max - min) + min) / step) * step;
                input.value = randomValue.toFixed(3); // Устанавливаем значение в инпут с округлением до 3 знаков
            });
        }