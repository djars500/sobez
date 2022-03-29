const button = document.getElementById('menu-burger');
const sidebar = document.getElementById('sidebar');
const content = document.getElementById('content');

button.addEventListener('click',(event)=>{
    console.log(event,'clicked');
    sidebar.classList.toggle('disabled');
    content.classList.toggle('larged');
})