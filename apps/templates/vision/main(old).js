const dragArea = document.querySelectorAll('.drag-area');
const dragText = document.querySelector('.header');
let file;


dragArea.addEventListener('dragover', (event) => {
    event.preventDefault();
    dragText.textContent = 'Release to Upload';
    dragArea.classList.add('active');
});

dragArea.addEventListener('dragleave', (e) => {
    dragText.textContent = 'Drag &  Drop'
    dragArea.classList.remove('active');

});


dragArea.addEventListener('drop',(event) => {
    event.preventDefault();

    file = event.dataTransfer.files[0];
    let fileType = file.type;
    let validExtensions = ['image/jpeg', 'image/jpg', 'image/png']


    if(validExtensions.includes(fileType)){
        let fileReader = new FileReader();

        fileReader.onload = () => {
            let fileURL = fileReader.result;
            // console.log(fileURL);

            // let imgTag = ;
            dragArea.innerHTML = <img src=`${fileURL}` alt='' >;
        }   
        fileReader.readAsDataURL(file)
    }
    else{
        alert('Please select a image file');
        dragArea.classList.remove('active');
    }
});