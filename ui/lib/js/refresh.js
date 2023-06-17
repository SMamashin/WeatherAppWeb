const refreshButton = document.querySelector('.refresh');

const refreshPage = () => {
  location.reload();
}

refreshButton.addEventListener('click', refreshPage)