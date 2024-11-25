function result = factorial_recursive(n)
    % Recursive factorial calculation
    if n == 0
        result = 1;
    else
        result = n * factorial_recursive(n-1);
    end
end

function roots = quadratic_roots(a, b, c)
    % Calculate roots of a quadratic equation ax^2 + bx + c = 0
    discriminant = b^2 - 4*a*c;
    if discriminant > 0
        root1 = (-b + sqrt(discriminant)) / (2*a);
        root2 = (-b - sqrt(discriminant)) / (2*a);
    elseif discriminant == 0
        root1 = -b / (2*a);
        root2 = root1;  

    else
        real_part = -b / (2*a);
        imag_part = sqrt(-discriminant) / (2*a);
        root1 = complex(real_part, imag_part);
        root2 = complex(real_part, -imag_part);
    end
    roots = [root1, root2];
end

function area = heron_formula(a, b, c)
    % Calculate area of a triangle using Heron's formula
    s = (a + b + c) / 2;
    area = sqrt(s * (s - a) * (s - b) * (s - c));
end

function fib_series = fibonacci(n)
    % Generate Fibonacci series up to the nth term
    fib_series = zeros(1, n);
    fib_series(1) = 1;
    fib_series(2) = 1;
    for i = 3:n
        fib_series(i) = fib_series(i-1) + fib_series(i-2);
    end
end


fileID = fopen('matlab_output.txt','w');
% Test the functions
result = factorial_recursive(5);
fprintf(fileID, [num2str(result),'\n']);

roots = quadratic_roots(1, -3, 2);
fprintf(fileID, [num2str(roots), '\n']);

area = heron_formula(3, 4, 5);
fprintf(fileID, [num2str(area), '\n']);

fib_series = fibonacci(10);
fprintf(fileID, [num2str(fib_series), '\n']);








