// Button
let button = document.getElementById('submit')

// Select
let type = document.getElementById('id_content_type')

// Fields
let isbn = document.getElementById('id_isbn')
let url = document.getElementById('id_url')

let setVisibility = (value) => {
  button.removeAttribute('disabled')
  switch (value) {
    case '0':
      isbn.parentElement.parentElement.removeAttribute('hidden')
      url.parentElement.parentElement.setAttribute('hidden', true)
      break
      case '1':
      isbn.parentElement.parentElement.setAttribute('hidden', true)
      url.parentElement.parentElement.removeAttribute('hidden')
      break
    default:
      isbn.parentElement.parentElement.setAttribute('hidden', true)
      url.parentElement.parentElement.setAttribute('hidden', true)
      button.setAttribute('disabled', true)
      break
  }
}

type.onchange = (event) => setVisibility(event.target.value)

setVisibility(type.value)
