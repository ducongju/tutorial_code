import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

choose = 1

if choose == 1:
    plt.figure(figsize=(10, 10), dpi = 80)
    t = np.arange(0., 5., 0.2)
    # t = list(range(10))
    plt.plot(t, t, 'r-',
             t, t ** 2, 'bs',
             t, t ** 3, 'g^')
    plt.axis([0, 6, 0, 120])
    plt.xlabel('some numbers')
    plt.ylabel('some numbers')

    plt.show()

# 子图
elif choose == 2:
    def f(t):
        return np.exp(-t) * np.cos(2 * np.pi * t)

    plt.figure(1)
    plt.subplot(311)
    t1 = np.arange(0.0, 5.0, 0.1)
    t2 = np.arange(0.0, 5.0, 0.02)
    plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

    plt.subplot(312)
    mu, sigma = 100, 15
    x = mu + sigma * np.random.randn(10000)
    n, bins, patches = plt.hist(x, 50, density=1, facecolor='g', alpha=0.75)

    plt.xlabel('Smarts')
    plt.ylabel('Probability')
    plt.title('Histogram of IQ')
    plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
    plt.axis([40, 160, 0, 0.03])
    plt.grid(True)

    plt.subplot(313)
    t = np.arange(0.0, 5.0, 0.01)
    s = np.cos(2 * np.pi * t)
    line, = plt.plot(t, s, lw=2)

    plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
                 arrowprops=dict(facecolor='black', shrink=0.05),
                 )
    plt.ylim(-2, 2)
    plt.legend([line], ['line'], bbox_to_anchor=(1, 1))

    plt.show()

# 图像
elif choose == 3:
    img = mpimg.imread('stinkbug.png')
    print(img.shape)
    print(img.dtype)

    plt.figure(1)
    plt.subplot(221)
    plt.imshow(img)

    lum_img = img[:, :, 0]
    plt.subplot(222)
    plt.imshow(lum_img)

    plt.subplot(223)
    imgplot = plt.imshow(lum_img)
    imgplot.set_cmap('hot')

    plt.subplot(224)
    imgplot = plt.imshow(lum_img)
    imgplot.set_cmap('Spectral')
    imgplot.set_clim(0.0, 0.7)
    plt.colorbar()

    plt.show()
