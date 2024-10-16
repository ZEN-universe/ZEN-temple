import{s as at,e as g,c as h,b as w,f,y as wt,o as b,i as Y,h as u,z as Xe,A as Ze,n as $e,B as kt,C as Et,G as yt,t as Dt,a as M,d as Ct,g as O,D as xe,j as It,E as Vt,r as S,m as ne,v as Oe,w as j,F as et}from"../chunks/scheduler.Bjr9RZaN.js";import{S as it,i as rt,b as z,c as he,d as be,m as ve,t as $,a as le,e as Tt,f as me,g as Ht}from"../chunks/index.NoFf4Nre.js";import{S as Lt,B as Mt,b as Ot,c as St,f as jt}from"../chunks/utils.DeIKiDqC.js";import{e as tt}from"../chunks/each.D6YF6ztN.js";function ot(e,n,o){const r=e.slice();return r[8]=n[o],r}function nt(e){let n,o=e[8]+"",r,i,m;return{c(){n=g("option"),r=Dt(o),i=M(),this.h()},l(c){n=h(c,"OPTION",{});var l=w(n);r=Ct(l,o),i=O(l),l.forEach(f),this.h()},h(){n.__value=m=e[8],xe(n,n.__value)},m(c,l){Y(c,n,l),u(n,r),u(n,i)},p(c,l){l&2&&o!==(o=c[8]+"")&&It(r,o),l&2&&m!==(m=c[8])&&(n.__value=m,xe(n,n.__value))},d(c){c&&f(n)}}}function zt(e){let n,o,r,i,m,c=tt(e[1]),l=[];for(let s=0;s<c.length;s+=1)l[s]=nt(ot(e,c,s));return{c(){n=g("div"),o=g("select");for(let s=0;s<l.length;s+=1)l[s].c();this.h()},l(s){n=h(s,"DIV",{class:!0});var _=w(n);o=h(_,"SELECT",{});var d=w(o);for(let y=0;y<l.length;y+=1)l[y].l(d);d.forEach(f),_.forEach(f),this.h()},h(){o.disabled=r=!e[2],e[0]===void 0&&wt(()=>e[4].call(o)),b(n,"class","dropdown")},m(s,_){Y(s,n,_),u(n,o);for(let d=0;d<l.length;d+=1)l[d]&&l[d].m(o,null);Xe(o,e[0],!0),i||(m=[Ze(o,"change",e[4]),Ze(o,"change",e[5])],i=!0)},p(s,[_]){if(_&2){c=tt(s[1]);let d;for(d=0;d<c.length;d+=1){const y=ot(s,c,d);l[d]?l[d].p(y,_):(l[d]=nt(y),l[d].c(),l[d].m(o,null))}for(;d<l.length;d+=1)l[d].d(1);l.length=c.length}_&4&&r!==(r=!s[2])&&(o.disabled=r),_&3&&Xe(o,s[0])},i:$e,o:$e,d(s){s&&f(n),kt(l,s),i=!1,Et(m)}}}function Bt(e,n,o){let{options:r}=n,{selected_option:i=r[0]}=n,{enabled:m=!0}=n;r.join("_");const c=yt();function l(){c("selection-changed",i)}function s(){i=Vt(this),o(0,i),o(1,r)}const _=()=>l();return e.$$set=d=>{"options"in d&&o(1,r=d.options),"selected_option"in d&&o(0,i=d.selected_option),"enabled"in d&&o(2,m=d.enabled)},[i,r,m,l,s,_]}class Ne extends it{constructor(n){super(),rt(this,n,Bt,zt,at,{options:1,selected_option:0,enabled:2})}}function lt(e){let n,o='<div class="spinner-border center" role="status"><span class="visually-hidden">Loading...</span></div>';return{c(){n=g("div"),n.innerHTML=o,this.h()},l(r){n=h(r,"DIV",{class:!0,"data-svelte-h":!0}),ne(n)!=="svelte-57s7b4"&&(n.innerHTML=o),this.h()},h(){b(n,"class","text-center")},m(r,i){Y(r,n,i)},d(r){r&&f(n)}}}function st(e){let n,o,r,i;function m(l){e[24](l)}let c={zoom:!0};return e[10]!==void 0&&(c.config=e[10]),o=new Mt({props:c}),S.push(()=>z(o,"config",m)),{c(){n=g("div"),he(o.$$.fragment),this.h()},l(l){n=h(l,"DIV",{style:!0});var s=w(n);be(o.$$.fragment,s),s.forEach(f),this.h()},h(){Oe(n,"position","relative")},m(l,s){Y(l,n,s),ve(o,n,null),i=!0},p(l,s){const _={};!r&&s&1024&&(r=!0,_.config=l[10],j(()=>r=!1)),o.$set(_)},i(l){i||($(o.$$.fragment,l),i=!0)},o(l){le(o.$$.fragment,l),i=!1},d(l){l&&f(n),me(o)}}}function Pt(e){let n,o='<div class="col"><h2>The Energy Balance</h2></div>',r,i,m,c,l,s,_,d='<button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">Solution Selection</button>',y,I,H,D,se,T,fe,ae,_e,pe,q,W,we='<button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">Data selection</button>',ge,F,L,J,G,Q,ke="Year",p,E,Ee,x,ee,U,C,A,ye="Node",ie,a,X,Se,je,re,Z,de,We="Carrier",ze,B,Be,Pe,De,te,P,Ce,Ie;function dt(t){e[13](t)}function ct(t){e[14](t)}function ut(t){e[15](t)}function ft(t){e[16](t)}function _t(t){e[17](t)}let ce={enabled:!e[2]&&!e[3]};e[6]!==void 0&&(ce.carriers=e[6]),e[4]!==void 0&&(ce.nodes=e[4]),e[8]!==void 0&&(ce.years=e[8]),e[0]!==void 0&&(ce.selected_solution=e[0]),e[2]!==void 0&&(ce.loading=e[2]),D=new Lt({props:ce}),S.push(()=>z(D,"carriers",dt)),S.push(()=>z(D,"nodes",ct)),S.push(()=>z(D,"years",ut)),S.push(()=>z(D,"selected_solution",ft)),S.push(()=>z(D,"loading",_t)),D.$on("solution_selected",e[11]);function pt(t){e[18](t)}function gt(t){e[19](t)}let qe={enabled:!e[3]&&!e[2]};e[8]!==void 0&&(qe.options=e[8]),e[9]!==void 0&&(qe.selected_option=e[9]),E=new Ne({props:qe}),S.push(()=>z(E,"options",pt)),S.push(()=>z(E,"selected_option",gt)),E.$on("selection-changed",e[12]);function ht(t){e[20](t)}function bt(t){e[21](t)}let Fe={enabled:!e[3]&&!e[2]};e[4]!==void 0&&(Fe.options=e[4]),e[5]!==void 0&&(Fe.selected_option=e[5]),a=new Ne({props:Fe}),S.push(()=>z(a,"options",ht)),S.push(()=>z(a,"selected_option",bt)),a.$on("selection-changed",e[12]);function vt(t){e[22](t)}function mt(t){e[23](t)}let Ge={enabled:!e[3]&&!e[2]};e[6]!==void 0&&(Ge.options=e[6]),e[7]!==void 0&&(Ge.selected_option=e[7]),B=new Ne({props:Ge}),S.push(()=>z(B,"options",vt)),S.push(()=>z(B,"selected_option",mt)),B.$on("selection-changed",e[12]);let V=e[3]&&lt(),k=!e[3]&&e[1]&&st(e);return{c(){n=g("div"),n.innerHTML=o,r=M(),i=g("div"),m=g("div"),c=g("div"),l=g("div"),s=g("div"),_=g("h2"),_.innerHTML=d,y=M(),I=g("div"),H=g("div"),he(D.$$.fragment),pe=M(),q=g("div"),W=g("h2"),W.innerHTML=we,ge=M(),F=g("div"),L=g("div"),J=g("div"),G=g("div"),Q=g("h3"),Q.textContent=ke,p=M(),he(E.$$.fragment),ee=M(),U=g("div"),C=g("div"),A=g("h3"),A.textContent=ye,ie=M(),he(a.$$.fragment),je=M(),re=g("div"),Z=g("div"),de=g("h3"),de.textContent=We,ze=M(),he(B.$$.fragment),De=M(),te=g("div"),P=g("div"),V&&V.c(),Ce=M(),k&&k.c(),this.h()},l(t){n=h(t,"DIV",{class:!0,"data-svelte-h":!0}),ne(n)!=="svelte-1d6fcfp"&&(n.innerHTML=o),r=O(t),i=h(t,"DIV",{class:!0});var v=w(i);m=h(v,"DIV",{class:!0});var N=w(m);c=h(N,"DIV",{class:!0,style:!0});var oe=w(c);l=h(oe,"DIV",{class:!0,id:!0});var K=w(l);s=h(K,"DIV",{class:!0});var R=w(s);_=h(R,"H2",{class:!0,"data-svelte-h":!0}),ne(_)!=="svelte-1oln34a"&&(_.innerHTML=d),y=O(R),I=h(R,"DIV",{id:!0,class:!0,"data-bs-parent":!0});var Ae=w(I);H=h(Ae,"DIV",{class:!0});var Ke=w(H);be(D.$$.fragment,Ke),Ke.forEach(f),Ae.forEach(f),R.forEach(f),pe=O(K),q=h(K,"DIV",{class:!0});var Ve=w(q);W=h(Ve,"H2",{class:!0,"data-svelte-h":!0}),ne(W)!=="svelte-1huxmzt"&&(W.innerHTML=we),ge=O(Ve),F=h(Ve,"DIV",{id:!0,class:!0,"data-bs-parent":!0});var Re=w(F);L=h(Re,"DIV",{class:!0});var ue=w(L);J=h(ue,"DIV",{class:!0});var Ye=w(J);G=h(Ye,"DIV",{class:!0});var Te=w(G);Q=h(Te,"H3",{"data-svelte-h":!0}),ne(Q)!=="svelte-r9e7qt"&&(Q.textContent=ke),p=O(Te),be(E.$$.fragment,Te),Te.forEach(f),Ye.forEach(f),ee=O(ue),U=h(ue,"DIV",{class:!0});var Je=w(U);C=h(Je,"DIV",{class:!0});var He=w(C);A=h(He,"H3",{"data-svelte-h":!0}),ne(A)!=="svelte-ocjo5w"&&(A.textContent=ye),ie=O(He),be(a.$$.fragment,He),He.forEach(f),Je.forEach(f),je=O(ue),re=h(ue,"DIV",{class:!0});var Qe=w(re);Z=h(Qe,"DIV",{class:!0});var Le=w(Z);de=h(Le,"H3",{"data-svelte-h":!0}),ne(de)!=="svelte-xc22hm"&&(de.textContent=We),ze=O(Le),be(B.$$.fragment,Le),Le.forEach(f),Qe.forEach(f),ue.forEach(f),Re.forEach(f),Ve.forEach(f),K.forEach(f),oe.forEach(f),N.forEach(f),v.forEach(f),De=O(t),te=h(t,"DIV",{class:!0});var Ue=w(te);P=h(Ue,"DIV",{class:!0,style:!0});var Me=w(P);V&&V.l(Me),Ce=O(Me),k&&k.l(Me),Me.forEach(f),Ue.forEach(f),this.h()},h(){b(n,"class","row"),b(_,"class","accordion-header"),b(H,"class","accordion-body"),b(I,"id","collapseOne"),b(I,"class","accordion-collapse collapse show"),b(I,"data-bs-parent","#accordionExample"),b(s,"class","accordion-item solution-selection"),b(W,"class","accordion-header"),b(G,"class","col-6"),b(J,"class","row"),b(C,"class","col-6"),b(U,"class","row"),b(Z,"class","col-6"),b(re,"class","row"),b(L,"class","accordion-body"),b(F,"id","collapseTwo"),b(F,"class","accordion-collapse collapse"),b(F,"data-bs-parent","#accordionExample"),b(q,"class","accordion-item"),b(l,"class","accordion"),b(l,"id","accordionExample"),b(c,"class","filters"),Oe(c,"position","absolute"),Oe(c,"width","100%"),b(m,"class","col position-relative"),b(i,"class","row"),b(P,"class","col"),Oe(P,"margin-top","400px"),b(te,"class","row")},m(t,v){Y(t,n,v),Y(t,r,v),Y(t,i,v),u(i,m),u(m,c),u(c,l),u(l,s),u(s,_),u(s,y),u(s,I),u(I,H),ve(D,H,null),u(l,pe),u(l,q),u(q,W),u(q,ge),u(q,F),u(F,L),u(L,J),u(J,G),u(G,Q),u(G,p),ve(E,G,null),u(L,ee),u(L,U),u(U,C),u(C,A),u(C,ie),ve(a,C,null),u(L,je),u(L,re),u(re,Z),u(Z,de),u(Z,ze),ve(B,Z,null),Y(t,De,v),Y(t,te,v),u(te,P),V&&V.m(P,null),u(P,Ce),k&&k.m(P,null),Ie=!0},p(t,[v]){const N={};v&12&&(N.enabled=!t[2]&&!t[3]),!se&&v&64&&(se=!0,N.carriers=t[6],j(()=>se=!1)),!T&&v&16&&(T=!0,N.nodes=t[4],j(()=>T=!1)),!fe&&v&256&&(fe=!0,N.years=t[8],j(()=>fe=!1)),!ae&&v&1&&(ae=!0,N.selected_solution=t[0],j(()=>ae=!1)),!_e&&v&4&&(_e=!0,N.loading=t[2],j(()=>_e=!1)),D.$set(N);const oe={};v&12&&(oe.enabled=!t[3]&&!t[2]),!Ee&&v&256&&(Ee=!0,oe.options=t[8],j(()=>Ee=!1)),!x&&v&512&&(x=!0,oe.selected_option=t[9],j(()=>x=!1)),E.$set(oe);const K={};v&12&&(K.enabled=!t[3]&&!t[2]),!X&&v&16&&(X=!0,K.options=t[4],j(()=>X=!1)),!Se&&v&32&&(Se=!0,K.selected_option=t[5],j(()=>Se=!1)),a.$set(K);const R={};v&12&&(R.enabled=!t[3]&&!t[2]),!Be&&v&64&&(Be=!0,R.options=t[6],j(()=>Be=!1)),!Pe&&v&128&&(Pe=!0,R.selected_option=t[7],j(()=>Pe=!1)),B.$set(R),t[3]?V||(V=lt(),V.c(),V.m(P,Ce)):V&&(V.d(1),V=null),!t[3]&&t[1]?k?(k.p(t,v),v&10&&$(k,1)):(k=st(t),k.c(),$(k,1),k.m(P,null)):k&&(Ht(),le(k,1,1,()=>{k=null}),Tt())},i(t){Ie||($(D.$$.fragment,t),$(E.$$.fragment,t),$(a.$$.fragment,t),$(B.$$.fragment,t),$(k),Ie=!0)},o(t){le(D.$$.fragment,t),le(E.$$.fragment,t),le(a.$$.fragment,t),le(B.$$.fragment,t),le(k),Ie=!1},d(t){t&&(f(n),f(r),f(i),f(De),f(te)),me(D),me(E),me(a),me(B),V&&V.d(),k&&k.d()}}}function qt(e,n,o){var r=["rgb(75, 192, 192)","rgb(54, 162, 235)","rgb(255, 206, 86)","rgb(153, 102, 255)","rgb(255, 159, 64)","rgb(255, 99, 132)","rgb(201, 203, 207)","rgb(220,20,60)","rgb(255,99,71)","rgb(255,69,0)","rgb(154,205,50)","rgb(0,100,0)","rgb(50,205,50)","rgb(0,139,139)","rgb(153,50,204)","rgb(255,105,180)"];let i=null,m=!1,c=!1,l=!1,s=[],_=null,d=[],y=null,I=[],H=null,D="";const se={counter:1,type:"line",data:{datasets:[]},options:{animation:!1,normalized:!0,elements:{point:{radius:0}},responsive:!0,scales:{x:{stacked:!0,title:{display:!0,text:"Time"}},y:{stacked:!0,title:{display:!0,text:"Power"}}},borderWidth:1,plugins:{zoom:{pan:{enabled:!0,modifierKey:"ctrl",mode:"x"},zoom:{drag:{enabled:!0},wheel:{enabled:!0},mode:"x"}}}}};let T=structuredClone(se);async function fe(){i&&(o(10,T=structuredClone(se)),o(5,_=s[0]),o(7,y=d[0]),o(9,H=I[0]),o(1,m=!1),await ae())}async function ae(){if(o(3,l=!0),et(),_==null||y==null||H==null||i==null){o(3,l=!1);return}let p=Math.floor((H-i.detail.system.reference_year)/i.detail.system.interval_between_years);console.log("Getting energy balance.");let E=await Ot(i.solution_name,_,y,i.scenario_name,p);D=(await St(i.solution_name,"flow_export",i.scenario_name)).data[0][0];let x=[],ee=0;for(const C in E){let A={node:[_]};if(E[C]==null||E[C].data.length==0)continue;if("technology"in E[C].data[0]){let a=[];for(const X of E[C].data)a.push(X.technology);A={technology:a}}let ye={},ie=jt(E[C].data,A,ye);if(ie.length!=0)for(let a of ie){if(Object.keys(a.data).length==0)continue;switch(C){case"flow_storage_discharge":a.label=a.label+" (discharge)";break;case"flow_transport_in":a.label=a.label+" (transport in)";break;case"flow_import":a.label="Import";break;case"shed_demand":a.label="Shed Demand";break;case"flow_storage_charge":a.label=a.label+" (charge)";break;case"flow_transport_out":a.label=a.label+" (transport out)";break;case"flow_export":a.label="Export";break}let X="line";Object.keys(a.data).length==1&&(X="bar"),C=="demand"?(a.label="Demand",a.type="line",a.stack="ownCustomStack",a.fill=!1,a.borderColor="black",a.backgroundColor="white",a.borderWidth=2,a.stepped=!0,Object.keys(a.data).length==1&&(a.pointRadius=2)):(a.type=X,a.fill="origin",a.borderColor=r[ee%r.length],a.backgroundColor=r[ee%r.length].replace(")",", 1)"),a.stepped=!0,a.cubicInterpolationMode="monotone"),x.push(a),ee++}}o(10,T.data.labels=Object.keys(x[0].data),T),o(10,T.data.datasets=x,T),o(10,T.options.scales.y.title.text="Power ["+D+"]",T),o(3,l=!1),o(1,m=!0);let U=performance.now();await et(),console.log("Building plot took",performance.now()-U)}function _e(p){d=p,o(6,d)}function pe(p){s=p,o(4,s)}function q(p){I=p,o(8,I)}function W(p){i=p,o(0,i)}function we(p){c=p,o(2,c)}function ge(p){I=p,o(8,I)}function F(p){H=p,o(9,H)}function L(p){s=p,o(4,s)}function J(p){_=p,o(5,_)}function G(p){d=p,o(6,d)}function Q(p){y=p,o(7,y)}function ke(p){T=p,o(10,T)}return[i,m,c,l,s,_,d,y,I,H,T,fe,ae,_e,pe,q,W,we,ge,F,L,J,G,Q,ke]}class At extends it{constructor(n){super(),rt(this,n,qt,Pt,at,{})}}export{At as component};
