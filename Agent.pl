% Agent.pl

% implements Agent’s reset due to arriving into a cell inhabited by the Wumpus
reborn:-
assertz(hasarrow),
retractall(visited(_,_)),
assertz(visited(0,0)),
retractall(tingle(_,_)),
retractall(glitter(_,_)),
retractall(stench(_,_)),
retractall(current(_,_,_)),
retractall(wall(_,_,_)),
retractall(safeToVisit(_,_)),
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
:- dynamic safeToVisit/2.


action(V) :- 
member(V,[shoot,moveforward,turnleft,turnright,pickup]).




move(A,L) :-

(A == shoot, hasarrow, nth0(5,L,on), retractall(hasarrow),retractall(wumpusalive));
(A == shoot, hasarrow, nth0(5,L,off), retractall(hasarrow));
(A == moveforward, nth0(0,L,on), reposition(L));
(A == moveforward, nth0(4,L,off), current(X,Y,D), forward(X,Y,D), updateKB(L));
(A == moveforward, nth0(4,L,on),current(X,Y,D), getForward(X,Y,D,X2,Y2), assertz(wall(X2,Y2)));
(A == turnleft, current(X,Y,D),turnLeft(D,N),retractall(current(_,_,_)),assertz(current(X,Y,N)));
(A == turnright, current(X,Y,D),turnRight(D,N),retractall(current(_,_,_)),assertz(current(X,Y,N)));
(A == pickup, current(X,Y,D), nth0(3,L,on), reatractall(glitter(X,Y))).


adjacent(X1,Y1,X2,Y2) :-
X1 is X2, Y1 is Y2-1;
X1 is X2, Y1 is Y2+1;
Y1 is Y2, X1 is X2-1;
Y1 is Y2, X1 is X2+1 .


updateKB(L) :-
updateS(L),
updateT(L),
updateW(L),
updateG(L),
updateAbsSafe.


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
 
updateAbsSafe:-

current(X,Y,D),
Xminus is X-1,
Xplus is X+1,
Yminus is Y-1,
Yplus is Y+1,
(safe(Xminus,Y) -> assertz(safeToVisit(Xminus,Y)); true),
(safe(Xplus,Y) -> assertz(safeToVisit(Xplus,Y)); true),
(safe(X,Yminus) -> assertz(safeToVisit(X,Yminus)); true),
(safe(X,Yplus) -> assertz(safeToVisit(X,Yplus)); true).

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
(D == rnorth -> (retractall(current(_,_,_)),K is Y+1, assertz(current(X,K,D)), assertz(visited(X,K)));
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


safe(X,Y):-
 (\+wumpus(X,Y),\+confundus(X,Y), nextToVisited(X,Y));
 visited(X,Y).
 

nextToVisited(X,Y) :-
 Xminus is X-1,
 Xplus is X+1,
 Yminus is Y-1,
 Yplus is Y+1,
 (visited(Xminus,Y);
 visited(Xplus,Y);
 visited(X,Yminus);
 visited(X,Yplus)).

wumpus(X,Y) :-
 wumpusalive,
 \+visited(X,Y),
 Xminus is X-1,
 Xplus is X+1,
 Yminus is Y-1,
 Yplus is Y+1,
 checkW(X,Y),
 (stench(Xminus,Y);
  stench(Xplus, Y);
  stench(X, Yplus);
  stench(X, Yminus)
  ).
 
 checkW(X,Y) :-
 Xminus is X-1,
 Xplus is X+1,
 Yminus is Y-1,
 Yplus is Y+1,
 \+((visited(Xminus,Y),\+stench(Xminus,Y));
     (visited(Xplus, Y), \+stench(Xplus, Y));
     (visited(X, Yminus), \+stench(X, Yminus));
     (visited(X, Yplus), \+stench(X, Yplus))).


confundus(X,Y) :-
\+visited(X,Y),
Xminus is X-1,
Xplus is X+1,
Yminus is Y-1,
Yplus is Y+1,
 checkC(X,Y),
(tingle(Xminus,Y);
 tingle(Xplus, Y);
 tingle(X, Yplus);
 tingle(X, Yminus)
 ).
 
 checkC(X,Y) :-
 Xminus is X-1,
 Xplus is X+1,
 Yminus is Y-1,
 Yplus is Y+1,
 \+((visited(Xminus,Y),\+stench(Xminus,Y));
     (visited(Xplus, Y), \+stench(Xplus, Y));
     (visited(X, Yminus), \+stench(X, Yminus));
     (visited(X, Yplus), \+stench(X, Yplus))).

 %explorePath(X,Y,D,P) :-
  X == 0,
  Y == 0,
  \+(safeToVisit(XSafe,YSafe),\+(visitesd(XSafe,YSafe))),
  \+glitter(G1,G2),
 P = [].
 
 explorePath(X,Y,D,P) :-
 \+(visited(X,Y)),
P = [].
 
 
 explorePath(X,Y,D,[H|Q]) :-
 getForward(X,Y,D,X2,Y2),
 \+(visited(X2,Y2)),
 safe(X2,Y2),
 H = moveforward,
 explorePath(X2,Y2,D,Q).
 
 explorePath(X,Y,D,[H|Q]) :-
 getLeft(X,Y,D,X2,Y2),
 \+(visited(X2,Y2)),
 safe(X2,Y2),
 H = turnleft,
 explorePath(X,Y,D,Q).
 
 explorePath(X,Y,D,[H|Q]) :-
 getRight(X,Y,D,X2,Y2),
 \+(visited(X2,Y2)),
 safe(X2,Y2),
 H = turnright,
 explorePath(X,Y,D,Q).

 explorePath(X,Y,D,[H|Q]) :-
  getForward(X,Y,D,X2,Y2),
visited(X2,Y2),
H = moveforward,
explorePath(X2,Y2,D,Q).

 explorePath(X,Y,D,[H|Q]) :-
  getLeft(X,Y,D,X2,Y2),
visited(X2,Y2),
H = turnleft,
explorePath(X,Y,D,Q).

 explorePath(X,Y,D,[H|Q]) :-
  getRight(X,Y,D,X2,Y2),
visited(X2,Y2),
H = turnright,
explorePath(X,Y,D,Q).
 
%The agent needs to turn back
explorePath(X,Y,D,[H|Q]) :-
H = turnright,
explorePath(X,Y,D,Q).
 
explore(L) :-
current(X,Y,D),
 explorePath(X,Y,D,L).
 
 


%change of direction
turnLeft(rnorth,rwest).
turnLeft(rwest,rsouth).
turnLeft(rsouth,reast).
turnLeft(reast,rnorth).
turnRight(rnorth,reast).
turnRight(rwest,rnorth).
turnRight(rsouth,rwest).
turnRight(reast,rsouth).
