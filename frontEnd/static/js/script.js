fetch('http://desktop-43mqlbj.netbird.cloud:8000/main_menu/{number}')
    .then(response => {
        if(!response.ok) throw new Error('Ошибка сети');
        return response.json();
    })
    .then(data => console.log(data))