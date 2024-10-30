figure;

x = linspace(-2*pi, 2*pi, 240);
y_sin = sin(x);
y_cos = cos(x);

plot(x, y_sin);
hold on;
plot(x, y_cos);
hold off;

title('Plot of sine and cosine functions');
xlabel('-2\pi < x < 2\pi');
ylabel('sin(x) and cos(x)');
legend({'y = sin(x)', 'y = cos(x)'}, 'Location', 'northeast');
