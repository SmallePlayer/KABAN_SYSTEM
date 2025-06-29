fetch('http://127.0.0.1:8000/all_printers')
    .then(response => {
        if(!response.ok) throw new Error('Ошибка сети');
        return response.json();
    })
    .then(data => console.log(data))