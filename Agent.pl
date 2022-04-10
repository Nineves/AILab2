% Agent.pl

% implements Agent’s reset due to arriving into a cell inhabited by the Wumpus
reborn:-
assertz(hasarrow),
retractall(visited(_,_)),
assertz(visited(0,0)),
retractall(tingle(_,_)),
retractall(glitter(_,_)),
retractall(stench(_,_)),
retractall(safe(_,_)),
retractall(current(_,_,_)),
retractall(wall(_,_,_)),
assertz(current(0,0,rnorth)),
assertz(wumpusalive).


% implement Agent’s reasoning response to executing action A and receiving sensory input L.

:- dynamic hasarrow/0.
:- dynamic wumpusalive/0.
:- dynamic coins/0.
:- dynamic visited/2.
:- dynamic safe/2.
:- dynamic current/3.
:- dynamic tingle/2.
:- dynamic glitter/2.
:- dynamic stench/2.
:- dynamic safe/2.
:- dynamic tingle/2.
:- dynamic wall/2.
:- dynamic exploredPath/1.


action(V) :- 
member(V,[shoot,moveforward,turnleft,turnright,pickup]).



% L = [Confounded, Stench, Tingle, Glitter, Bump, Scream]
move(A,L) :-

(A == shoot, hasarrow, nth0(5,L,on), retractall(hasarrow)); 			% the wumpus is dead and the agent loses arrow.
(A == shoot, hasarrow, nth0(5,L,off), retractall(hasarrow);			% the agent loses arrow
(A == moveforward, nth0(0,L,on), reposition());
(A == moveforward, nth0(4,L,off), current(X,Y,D), forward(X,Y,D), updateKB(L));
(A == moveforward, nth0(4,L,on),current(X,Y,D), assertz(wall(X,Y)));
(A == turnleft, current(X,Y,D),turnLeft(D,N),retractall(current(_,_,_)),assertz(current(X,Y,N)));
(A == turnright, current(X,Y,D),turnRight(D,N),retractall(current(_,_,_)),assertz(current(X,Y,N)));
(A == pickup, current(X,Y,D), nth0(3,L,on) -> reatractall(glitter(X,Y))).



adjacent(X1,Y1,X2,Y2) :-
X1 is X2, Y1 is Y2-1 ;
X1 is X2, Y1 is Y2+1 ;
Y1 is Y2, X1 is X2-1 ;
Y1 is Y2, X1 is X2+1 .


updateKB(L) :-
updateS(L),
updateT(L),
updateW(L),
updateG(L),
checkSafe(L).


updateS(L) :-
nth0(1,L,on) -> (current(X,Y,D), assertz(stench(X,Y)));
nth0(1,L,off).

updateT(L) :-
nth0(2,L,on)-> (current(X,Y,D), assertz(tingle(X,Y)));
nth0(2,L,off).

updateW(L) :-
nth0(5,L,on)-> retractall(wumpusalive);
nth0(5,L,off).

updateG(L) :-
nth0(3,L,on)->(current(X,Y,D), assertz(glitter(X,Y)));
nth0(3,L,off).
 
checkSafe(L) :-
 Xminus is X-1,
 Xplus is X+1,
 Yminus is Y-1,
 Yplus is Y+1,
 nth0(1,L,off),nth0(2,L,off)-> assertz(safe(Xminus,Y)),assertz(safe(Xplus,Y)),assertz(safe(X,Yminus)),assertz(safe(X,Yplus));
 nth0(1,L,on);
 nth0(2,L,on).


getForward(X,Y,D,X2,Y2) :-
 
 D == rnorth -> (X2 is X, Y2 is Y+1);
 D == rwest -> (X2 is X-1, Y2 is Y);
 D == reast -> (X2 is X+1, Y2 is Y);
 D == rsouth -> (X2 is X, Y2 is Y-1).
 
 getLeft(X,Y,D,X2,Y2) :-
 
 D == rnorth -> (X2 is X-1, Y2 is Y);
 D == rwest -> (X2 is X, Y2 is Y-1);
 D == reast -> (X2 is X, Y2 is Y+1);
 D == rsouth -> (X2 is X+1, Y2 is Y).
 
 getRight(X,Y,D,X2,Y2) :-
 
 D == rnorth -> (X2 is X+1, Y2 is Y);
 D == rwest -> (X2 is X, Y2 is Y+1);
 D == reast -> (X2 is X, Y2 is Y-1);
 D == rsouth -> (X2 is X-1, Y2 is Y).
 
forward(X,Y,D) :-

current(X,Y,D),
(D == rnorth -> (retractall(current(_,_,_)),K is Y+1, assertz(current(X,K,D)), assertz(visited(X,Y)));
D == rwest -> (retractall(current(_,_,_)), K is X-1, assertz(current(K,Y,D)), assertz(visited(K,Y)));
D == reast -> (retractall(current(_,_,_)), K is X+1, assertz(current(K,Y,D)), assertz(visited(K,Y)));
D == rsouth -> (retractall(current(_,_,_)), K is Y-1, assertz(current(X,K,D)), assertz(visited(X,K)))).



%if the agent is in the same direction with the agent
inSameDirection(X,Y,D,X2,Y2):-

(D == rnorth, X==X2, Y2 > Y);
(D == rsouth, X==X2, Y2 < Y);
(D == rwest, Y==Y2, X2<X);
(D == reast, Y==Y2, X2>X).


reposition(L):-
nth(0,L,on),
retractall(visited(_,_)),
assertz(visited(0,0)),
retractall(current(_,_,_)),
asserts(current(0,0,rnorth)),
updateKB(L).


%initialize the agent
current(0,0,rnorth).
visited(0,0).
safe(0,0).


safe(X,Y) :-
 \+ wumpusalive.

wumpus(X,Y) :-
 wumpusalive,
 \+safe(X,Y),
 \+visited(X,Y),
 Xminus is X-1,
 Xplus is X+1,
 Yminus is Y-1,
 Yplus is Y+1,
 (stench(Xminus,Y);
  stench(Xplus, Y);
  stench(X, Yplus);
  stench(X, Yminus);
  ).

confundus(X,Y) :-
\+safe(X,Y),
\+visited(X,Y),
Xminus is X-1,
Xplus is X+1,
Yminus is Y-1,
Yplus is Y+1,
(tingle(Xminus,Y);
 tingle(Xplus, Y);
 tingle(X, Yplus);
 tingle(X, Yminus);
 ).

 explorePath(X,Y,D,P) :-
 /+ visited(X,Y),
 assertz(exploredPath(P)).
 
 explorePath(X,Y,D,P) :-
 /+ visited(X,Y),
 assertz(exploredPath(P)).
 
 explorePath(X,Y,D,P) :-
 getForward(X,Y,D,X2,Y2),
 /+visited(X2,Y2),
 safe(X2,Y2),
 append(P, ["moveforward"],newP),
 explorePath(X2,Y2,D,newP).
 
 explorePath(X,Y,D,P) :-
 getLeft(X,Y,D,X2,Y2),
 /+visited(X2,Y2),
 safe(X2,Y2),
 append(P, ["turnleft"],newP),
 explorePath(X2,Y2,D,newP).
 
 explorePath(X,Y,D,P) :-
 getRight(X,Y,D,X2,Y2),
 /+visited(X2,Y2),
 safe(X2,Y2),
 append(P, ["turnright"],newP),
 explorePath(X2,Y2,D,newP).
 

explore(L) :-
current(X,Y,D),
 explorePath(X,Y,D,[]).
 
 
 
%helper function
add(A,B,[A|B]).


%change of direction
turnLeft(rnorth,rwest).
turnLeft(rwest,rsouth).
turnLeft(rsouth,reast).
turnLeft(reast,rnorth).
turnRight(rnorth,reast).
turnRight(rwest,rnorth).
turnRight(rsouth,rwest).
turnRight(reast,rsouth).
