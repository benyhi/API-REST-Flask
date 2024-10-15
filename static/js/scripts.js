links = document.getElementsByClassName('nav-link')

Array.from(links).forEach(x => {
    x.addEventListener('click', () =>{
        x.classList.remove('selected')
        if (x.classList.contains('selected')){
            x.classList.remove('selected')
        } else{
            x.classList.add('selected')
        }
    })
});