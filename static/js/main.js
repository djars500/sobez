const button = document.getElementById('menu-burger');
const sidebar = document.getElementById('sidebar__category');
const content = document.getElementById('content');

button.addEventListener('click', (event) => {
    console.log(event, 'clicked');
    sidebar.classList.toggle('disabled');
    content.classList.toggle('larged');
})