
console.log(2222222);
const btnAdd = document.querySelector('#AddRecept'),
    ModalWindow = document.querySelector('.ShowModalWindow'),
    CloseModalBtn = document.querySelectorAll('.modal_close'),
    LoginButton = document.querySelector('#tab-login'),
    ReginButton = document.querySelector('#tab-register'),
    LoginInputs = document.querySelector('#pills-login'),
    ReginInputs = document.querySelector('#pills-register'),
    EditProfile = document.querySelector('#EditProfile'),
    ModalProfile = document.querySelector('#Profile');


if(btnAdd) {
    btnAdd.addEventListener('click', ()=>{
    document.body.style.overflow = 'hidden';
    ModalWindow.style.display = 'block';
    console.log(ModalWindow);
    console.log(11111);
    });
}

if(CloseModalBtn) {
    CloseModalBtn.forEach(element => {
        element.addEventListener('click', (e)=>{
            document.body.style.overflow = 'scroll';
            ModalWindow.style.display = 'none';
            ModalProfile.style.display = 'none';
        });
    });
}

if(LoginButton) {
    LoginButton.addEventListener('click', ()=>{
            console.log(11);
            ReginInputs.style.display = 'none';
            LoginInputs.style.display = 'block';
            ReginInputs.classList.remove('fade');
            LoginInputs.classList.add('active');
            ReginButton.classList.toggle('active');
            LoginButton.classList.toggle('active');
        });
}

if(ReginButton) {
    ReginButton.addEventListener('click', ()=>{
            console.log(22);
            LoginInputs.style.display = 'none';
            ReginInputs.style.display = 'block';
            ReginInputs.classList.remove('fade');
            LoginInputs.classList.add('active');
            LoginButton.classList.toggle('active');
            ReginButton.classList.toggle('active');
        });
}

if(EditProfile){
    EditProfile.addEventListener('click', ()=>{
        document.body.style.overflow = 'hidden';
        ModalProfile.style.display = 'block';
        console.log(11111);
        });
}

//     btnAdd.addEventListener('click', ()=>{
//         document.body.style.overflow = 'hidden';
//         ModalWindow.style.display = 'block';
//         console.log(ModalWindow);
//         console.log(11111);
//     });
    
//     CloseModalBtn.addEventListener('click', ()=>{
//         document.body.style.overflow = 'hidden';
//         ModalWindow.style.display = 'block';
//     });


// LoginButton.addEventListener('click', ()=>{
//     console.log(11);
//     ReginInputs.style.display = 'none';
//     LoginInputs.style.display = 'block';
//     ReginInputs.classList.remove('fade');
//     LoginInputs.classList.add('active');
//     ReginButton.classList.toggle('active');
//     LoginButton.classList.toggle('active');
// });
// ReginButton.addEventListener('click', ()=>{
//     console.log(22);
//     LoginInputs.style.display = 'none';
//     ReginInputs.style.display = 'block';
//     ReginInputs.classList.remove('fade');
//     LoginInputs.classList.add('active');
//     LoginButton.classList.toggle('active');
//     ReginButton.classList.toggle('active');
// });



