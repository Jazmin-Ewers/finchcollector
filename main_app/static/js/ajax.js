document.addEventListener('DOMContentLoaded', function() {
    document.addEventListener('dragenter', function(e) {
        if (e.target.className === 'lane droptarget') {
            e.target.style.background = 'blue'
        }

    })
    document.addEventListener('dragover', function(e){
        e.preventDefault()
    })
    document.addEventListener('dragleave', function(e){
        if (e.target.className === 'lane droptarget') {
            e.target.style.background = ''
        }

    })
})