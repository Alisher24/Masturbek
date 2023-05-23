console.log(22)
const btnAdd = document.querySelector('#AddRecept'),
 ModalWindow = document.querySelector('ShowModalWindow'),
    LoginButton = document.querySelector('#tab-login'),
    ReginButton = document.querySelector('#tab-register'),
    LoginInputs = document.querySelector('#pills-login'),
    ReginInputs = document.querySelector('#pills-register');

const showModal = ()=>{
    btnAdd.addEventListener('click', ()=>{
    document.body.style.overflow = 'hidden';
    ModalWindow.style.display = 'block';
    console.log(ModalWindow);
});
}

const ChangeTab = ()=>{

}
LoginButton.addEventListener('click', ()=>{

        console.log(11)
        ReginInputs.style.display = 'none';
        LoginInputs.style.display = 'block';
        ReginInputs.classList.remove('fade');
        LoginInputs.classList.add('active');
        ReginButton.classList.toggle('active');
        LoginButton.classList.toggle('active');
    });
ReginButton.addEventListener('click', ()=>{
        console.log(22);
        LoginInputs.style.display = 'none';
        ReginInputs.style.display = 'block';
        ReginInputs.classList.remove('fade');
        LoginInputs.classList.add('active');
        LoginButton.classList.toggle('active');
        ReginButton.classList.toggle('active');
    });
ChangeTab();
showModal();


