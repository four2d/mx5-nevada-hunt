document.documentElement.classList.add('js');
const nav=document.querySelector('.nav'),b=document.querySelector('.burger');
if(b){b.addEventListener('click',()=>{const o=nav.classList.toggle('open');b.setAttribute('aria-expanded',o)});nav.querySelectorAll('.links a').forEach(a=>a.addEventListener('click',()=>nav.classList.remove('open')))}
if('IntersectionObserver'in window){const o=new IntersectionObserver(e=>e.forEach(x=>{if(x.isIntersecting){x.target.classList.add('in');o.unobserve(x.target)}}),{threshold:.05});document.querySelectorAll('.rv').forEach(el=>o.observe(el))}else document.querySelectorAll('.rv').forEach(el=>el.classList.add('in'));
document.querySelectorAll('.gth').forEach(t=>t.addEventListener('click',()=>{const m=document.querySelector('.gmain picture');m.querySelector('source').srcset=t.dataset.webp;m.querySelector('img').src=t.dataset.jpg;document.querySelectorAll('.gth').forEach(x=>x.classList.remove('on'));t.classList.add('on')}));
setTimeout(()=>document.querySelectorAll('.rv').forEach(el=>el.classList.add('in')),1200);
