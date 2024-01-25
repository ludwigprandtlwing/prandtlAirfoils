% Verwyder geraas uit die HQ34 profiel se koördinate

pkg load splines;

close all;

% Lees in die vlerkprofiel se koördinate
[x, y] = lees_vlerkprofiel_in('hq34.dat');
% Plot die vlerkprofiel
figure(1);
plot(x, y); title('Vlerkprofiel soos afgetas van dokument'); hold on;
% Kies nou die punte wat gebruik gaan word vir die krommepassing:
kiespunte = [1 3 10 20 30 50 60 70 75 80 90 100 105 110 115 120 130 140 147 150 160 170 180 190 200 210 220 230 240 250 260 263];
x_pas = x(kiespunte);
y_pas = y(kiespunte);
% Plot die punte wat gekies is.
plot(x_pas, y_pas, 'ro');

% Doen gewone spline interpolasie en probeer dit.  Plot ou resultate bo-oor
figure(2);
hf = plot(x,y); hold on; title('Vergelyk spline oorspronklike punte');
% Plot datapunte
plot(x_pas, y_pas, 'ro');
% Doen spline passing
vlerk_profiel_gewone_spline = cscvn([x_pas;y_pas])
fnplt(vlerk_profiel_gewone_spline, 'r-');
% Kry nuwe punte uit
points = fnplt(vlerk_profiel_gewone_spline,'g',3);
plot(points(1, :),points(2, :), 'k-'); 
skryf_vlerkprofiel_uit('hq34_glad.dat', 'hq34', points(1, :), points(2, :));

% Print na eps/pdf
%print -deps foo.eps