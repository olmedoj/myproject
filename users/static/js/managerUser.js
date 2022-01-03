(function() {
    const btnDelete=document.querySelectorAll(".btnDelete");

btnDelete.forEach(btn=>{
    btn.addEventListener('click', (e)=>{
        const confirmation = confirm('Are you sure that do you want to delete this user?');
        if (!confirmation){
            e.preventDefault();
        }
    });
});

})();