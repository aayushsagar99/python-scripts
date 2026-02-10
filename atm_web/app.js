(function(){
  const PIN_CODE = '3867'; // Example PIN — change as needed
  let chances = 3;
  let balance = 67.14;
  const allowedWithdraw = [10,20,30,40,50,60,70,80,90,100];

  const el = id => document.getElementById(id);
  const qs = sel => document.querySelector(sel);

  const login = el('login');
  const menu = el('menu');
  const pinInput = el('pin');
  const loginBtn = el('loginBtn');
  const pinMsg = el('pinMsg');
  const actionArea = el('actionArea');
  const logoutBtn = el('logout');
  const serverLink = el('serverLink');

  function formatCurrency(v){return 'Rs. ' + v.toFixed(2)}

  function showMenu(){
    login.classList.add('hidden');
    menu.classList.remove('hidden');
    renderBalance();
  }

  function showLogin(){
    pinInput.value='';
    pinMsg.textContent='';
    menu.classList.add('hidden');
    login.classList.remove('hidden');
  }

  function renderBalance(){
    actionArea.innerHTML = `<p><strong>Balance:</strong> <span id=bal>${formatCurrency(balance)}</span></p>`;
  }

  function handleWithdraw(){
    actionArea.innerHTML = '';
    const div = document.createElement('div');
    div.innerHTML = '<p>Select amount to withdraw</p>';
    const btnRow = document.createElement('div'); btnRow.className='row';
    allowedWithdraw.forEach(a=>{
      const b = document.createElement('button'); b.className='amount-btn small'; b.textContent=a; b.addEventListener('click',()=>doWithdraw(a));
      btnRow.appendChild(b);
    });
    div.appendChild(btnRow);
    // custom amount
    const custom = document.createElement('div');
    custom.innerHTML = '<p>Or enter custom amount</p><input id="customAmt" type="number" min="0" step="1" placeholder="Amount" /><button id="doCustom">Withdraw</button><div id="wmsg" class="msg"></div>';
    div.appendChild(custom);
    actionArea.appendChild(div);
    el('doCustom').addEventListener('click',()=>{
      const v = Number(el('customAmt').value);
      if (!Number.isFinite(v) || v<=0){ el('wmsg').textContent='Enter a valid positive amount'; return }
      if (!allowedWithdraw.includes(v)){ el('wmsg').textContent='Allowed notes are: ' + allowedWithdraw.join(', '); return }
      doWithdraw(v);
    });
  }

  function doWithdraw(amount){
    if (amount>balance){ actionArea.innerHTML = '<div class="msg">Insufficient funds</div>'; return }
    balance -= amount;
    actionArea.innerHTML = `<div>Dispensing ${amount}. <br/>New balance: ${formatCurrency(balance)}</div>`;
  }

  function handleDeposit(){
    actionArea.innerHTML = '';
    const div = document.createElement('div');
    div.innerHTML = '<p>Enter amount to deposit</p><input id="depAmt" type="number" min="0" step="0.01" placeholder="Amount" /><button id="doDep">Deposit</button><div id="dmsg" class="msg"></div>';
    actionArea.appendChild(div);
    el('doDep').addEventListener('click',()=>{
      const v = Number(el('depAmt').value);
      if (!Number.isFinite(v) || v<=0){ el('dmsg').textContent='Enter a valid positive amount'; return }
      balance += v;
      actionArea.innerHTML = `<div>Deposited ${formatCurrency(v)}. <br/>New balance: ${formatCurrency(balance)}</div>`;
    });
  }

  document.addEventListener('click', e=>{
    const action = e.target && e.target.dataset && e.target.dataset.action;
    if (!action) return;
    if (action==='balance') renderBalance();
    if (action==='withdraw') handleWithdraw();
    if (action==='deposit') handleDeposit();
    if (action==='exit') { actionArea.innerHTML = '<div>Returning card... Thank you!</div>'; setTimeout(showLogin,1200); }
  });

  loginBtn.addEventListener('click', ()=>{
    const pin = pinInput.value.trim();
    if (pin===PIN_CODE){ showMenu(); return }
    chances -=1;
    if (chances<=0){ pinMsg.textContent='No more tries. Card retained.'; loginBtn.disabled=true; pinInput.disabled=true; return }
    pinMsg.textContent = `Incorrect PIN. ${chances} tries left.`;
  });

  logoutBtn.addEventListener('click', ()=>{
    chances = 3; showLogin();
  });

  // server link target (helpful when served)
  serverLink.href = './';

  // expose debug to console
  window._atm = {getBalance: ()=>balance};
})();
